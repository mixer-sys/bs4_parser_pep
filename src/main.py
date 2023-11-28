import logging
import re
from urllib.parse import urljoin

import requests_cache
from bs4 import BeautifulSoup
from tqdm import tqdm

from configs import configure_argument_parser, configure_logging
from constants import (BASE_DIR, EXPECTED_STATUS,
                       DOWNLOAD_FILE_PATTERN, FEATURES, HTMLTag,
                       LATEST_VERSIONS_RESULT_HEADER, MAIN_DOC_URL,
                       MAIN_PEP_URL, PEP_RESULT_HEADER,
                       VERSION_STATUS_PATTERN, WHATS_NEW_RESULT_HEADER)
from outputs import control_output
from utils import find_tag, get_response


def whats_new(session):
    whats_new_url = urljoin(MAIN_DOC_URL, 'whatsnew/')
    response = get_response(session, whats_new_url)
    if response is None:
        return
    soup = BeautifulSoup(response.text, features=FEATURES)
    main_div = find_tag(soup, HTMLTag.SECTION,
                        attrs={'id': 'what-s-new-in-python'})
    div_with_ul = find_tag(main_div, HTMLTag.DIV,
                           attrs={'class': 'toctree-wrapper'})
    sections_by_python = div_with_ul.find_all(HTMLTag.LI,
                                              attrs={'class': 'toctree-l1'})

    results = [WHATS_NEW_RESULT_HEADER]
    for section in tqdm(sections_by_python):
        version_a_tag = find_tag(section, HTMLTag.A)
        version_link = urljoin(whats_new_url, version_a_tag['href'])
        response = get_response(session, version_link)
        if response is None:
            continue

        soup = BeautifulSoup(response.text, features=FEATURES)
        h1 = find_tag(soup, HTMLTag.H1).text
        dl = find_tag(soup, HTMLTag.DL)
        dl_text = dl.text.replace('\n', ' ')

        results.append(
            (version_link, h1, dl_text)
        )

    return results


def latest_versions(session):
    response = get_response(session, MAIN_DOC_URL)
    if response is None:
        return

    soup = BeautifulSoup(response.text, features=FEATURES)
    sidebar = find_tag(soup, HTMLTag.DIV, {'class': 'sphinxsidebarwrapper'})
    ul_tags = sidebar.find_all(HTMLTag.UL)
    for ul in ul_tags:
        if 'All versions' in ul.text:
            a_tags = ul.find_all(HTMLTag.A)
            break
    else:
        raise Exception('Не найден список c версиями Python')

    results = [LATEST_VERSIONS_RESULT_HEADER]

    for a_tag in a_tags:
        link = a_tag['href']
        text_match = re.search(VERSION_STATUS_PATTERN, a_tag.text)
        if text_match is not None:
            version, status = text_match.groups()
        else:
            version, status = a_tag.text, ''
        results.append(
            (link, version, status)
        )

    return results


def download(session):
    downloads_url = urljoin(MAIN_DOC_URL, 'download.html')
    response = get_response(session, downloads_url)
    if response is None:
        return

    soup = BeautifulSoup(response.text, features=FEATURES)
    table_tag = find_tag(soup, HTMLTag.TABLE)
    pdf_a4_tag = find_tag(table_tag, HTMLTag.A,
                          {'href': re.compile(DOWNLOAD_FILE_PATTERN)})

    pdf_a4_link = pdf_a4_tag['href']
    archive_url = urljoin(downloads_url, pdf_a4_link)
    filename = archive_url.split('/')[-1]

    downloads_dir = BASE_DIR / 'downloads'
    downloads_dir.mkdir(exist_ok=True)
    archive_path = downloads_dir / filename

    response = session.get(archive_url)

    with open(archive_path, 'wb') as file:
        file.write(response.content)
    logging.info(f'Архив был загружен и сохранён: {archive_path}')


def pep(session):
    count_status = dict((key, 0) for key in EXPECTED_STATUS)
    results = [PEP_RESULT_HEADER]
    downloads_url = MAIN_PEP_URL

    response = get_response(session, downloads_url)
    if response is None:
        return

    soup = BeautifulSoup(response.text, features=FEATURES)
    table_tags = soup.find_all(
        HTMLTag.TABLE,
        attrs={'class': 'pep-zero-table docutils align-default'})

    for table_tag in tqdm(table_tags):
        rows = table_tag.find_all(
            HTMLTag.TR,
            attrs={'class': re.compile(r'(row-even|row-odd)')}
        )
        for row in tqdm(rows[1:]):
            global_status = ''
            if row.find(HTMLTag.ABBR):
                global_status = find_tag(row, HTMLTag.ABBR).text[1:]
            href = row.find(HTMLTag.A)['href']
            url = urljoin(MAIN_PEP_URL, href)
            response = get_response(session, url)
            if response is None:
                return
            soup = BeautifulSoup(response.text, features=FEATURES)
            local_status = find_tag(soup, HTMLTag.ABBR).text
            if local_status not in EXPECTED_STATUS[global_status]:
                logging.error(
                    'Несовпадающие статусы:\n'
                    f'{url}\n'
                    f'Статус в карточке: {local_status}\n'
                    f'Ожидаемые статусы: {EXPECTED_STATUS[global_status]}\n'
                )
            count_status[global_status] += 1
    for global_status in tqdm(count_status):
        results.append((global_status, count_status[global_status]))
    return results


MODE_TO_FUNCTION = {
    'whats-new': whats_new,
    'latest-versions': latest_versions,
    'download': download,
    'pep': pep
}


def main():
    configure_logging()
    logging.info('Парсер запущен!')

    arg_parser = configure_argument_parser(MODE_TO_FUNCTION.keys())
    args = arg_parser.parse_args()
    logging.info(f'Аргументы командной строки: {args}')

    session = requests_cache.CachedSession()
    if args.clear_cache:
        session.cache.clear()

    parser_mode = args.mode
    results = MODE_TO_FUNCTION[parser_mode](session)
    if results is not None:
        control_output(results, args)
    logging.info('Парсер завершил работу.')


if __name__ == '__main__':
    main()
