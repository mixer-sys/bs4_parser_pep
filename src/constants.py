from enum import Enum
from pathlib import Path

ENCODING = 'utf-8'
MAIN_DOC_URL = 'https://docs.python.org/3/'
MAIN_PEP_URL = 'https://peps.python.org/'
BASE_DIR = Path(__file__).parent
DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
LOG_FORMAT = '"%(asctime)s - [%(levelname)s] - %(message)s"'
DT_FORMAT = '%d.%m.%Y %H:%M:%S'

WHATS_NEW_RESULT_HEADER = ('Ссылка на статью', 'Заголовок', 'Редактор, Автор')
LATEST_VERSIONS_RESULT_HEADER = ('Ссылка на документацию', 'Версия', 'Статус')
PEP_RESULT_HEADER = ('Статус', 'Количество')
FEATURES = 'lxml'

# В строке типа 'Python 3.12 (stable)' найдет версию и статус, 3.12 и stable
VERSION_STATUS_PATTERN = r'Python (?P<version>\d\.\d+) \((?P<status>.*)\)'

# Найдет название файла, которое заканчивается на 'pdf-a4.zip'
DOWNLOAD_FILE_PATTERN = r'.+pdf-a4\.zip$'

EXPECTED_STATUS = {
    'A': ('Active', 'Accepted'),
    'D': ('Deferred',),
    'F': ('Final',),
    'P': ('Provisional',),
    'R': ('Rejected',),
    'S': ('Superseded',),
    'W': ('Withdrawn',),
    '': ('Draft', 'Active'),
}


class OutputType(str, Enum):
    PRETTY = 'pretty'
    FILE = 'file'


class HTMLTag:
    DIV = 'div'
    SECTION = 'section'
    LI = 'li'
    A = 'a'
    H1 = 'h1'
    DL = 'dl'
    UL = 'ul'
    TABLE = 'table'
    TR = 'tr'
    ABBR = 'abbr'
