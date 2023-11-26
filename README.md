# Проект парсинга pep

### Описание проекта:

Парсер статических страниц

### Как запустить проект:

Установить зависимости
```
python3 -m venv venv
source venv/Scripts/activate
pip3 install -r requirements.txt
```
### Возможности проекта:

```
$ python src/main.py -h
"26.11.2023 16:50:01 - [INFO] - Парсер запущен!"
usage: main.py [-h] [-c] [-o {pretty,file}] {whats-new,latest-versions,download,pep}

Парсер документации Python

positional arguments:
  {whats-new,latest-versions,download,pep}
                        Режимы работы парсера

optional arguments:
  -h, --help            show this help message and exit
  -c, --clear-cache     Очистка кеша
  -o {pretty,file}, --output {pretty,file}
                        Дополнительные способы вывода данных
```

### Описание режимов работы парсера
##### whats-new - парсит ссылки и авторов на документацию различных версий Python
##### latest-versions = парсит ссылки, версии, статус различных версий Python
##### download - парсит ссылку на загрузку файла и загружает его
##### pep - парсит статусы PEP и считает их количество 

### Примеры использования

```
$ python src/main.py pep -o pretty
"26.11.2023 17:13:28 - [INFO] - Парсер запущен!"
"26.11.2023 17:13:28 - [INFO] - Аргументы командной строки: Namespace(mode='pep', clear_cache=False, output='pretty')"
100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 17/17 [00:00<00:00, 20.94it/s]
100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 44/44 [00:01<00:00, 23.12it/s] 
100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 2/2 [00:00<00:00,  9.14it/s] 
100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 44/44 [00:03<00:00, 12.32it/s] 
100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 28/28 [00:01<00:00, 19.11it/s] 
100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 224/224 [00:12<00:00, 17.33it/s] 
100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 34/34 [00:01<00:00, 29.00it/s] 
100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 36/36 [00:02<00:00, 14.36it/s]
 73%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████▋                                                 | 8/11 [00:24<00:10,  3.63s/it]"26.11.2023 17:13:58 - [ERROR] - Несовпадающие статусы:██████████████████████████████▎                                                                                                   | 89/201 [00:04<00:08, 13.29it/s] 
https://peps.python.org/pep-0401/
Статус в карточке: April Fool!
Ожидаемые статусы: ('Rejected',)
"
100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 201/201 [00:11<00:00, 17.59it/s]
 82%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████                                 | 9/11 [00:36<00:12,  6.07s/it]"26.11.2023 17:14:10 - [ERROR] - Несовпадающие статусы:████▉                                                                                                                            | 191/630 [00:04<00:12, 35.11it/s] 
https://peps.python.org/pep-0401/
Статус в карточке: April Fool!
Ожидаемые статусы: ('Rejected',)
"
100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 630/630 [00:17<00:00, 36.43it/s]
100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00, 220.12it/s] 
100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 11/11 [00:53<00:00,  4.89s/it] 
100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 8/8 [00:00<?, ?it/s] 
+--------+------------+
| Статус | Количество |
+--------+------------+
| A      | 162        |
| D      | 72         |
| F      | 562        |
| P      | 4          |
| R      | 250        |
| S      | 40         |
| W      | 114        |
|        | 57         |
+--------+------------+
"26.11.2023 17:14:22 - [INFO] - Парсер завершил работу."
```

```
$ python src/main.py latest-versions -o pretty
"26.11.2023 17:07:06 - [INFO] - Парсер запущен!"
"26.11.2023 17:07:06 - [INFO] - Аргументы командной строки: Namespace(mode='latest-versions', clear_cache=False, output='pretty')"
+--------------------------------------+--------------+----------------+
| Ссылка на документацию               | Версия       | Статус         |
+--------------------------------------+--------------+----------------+
| https://docs.python.org/3.13/        | 3.13         | in development |
| https://docs.python.org/3.12/        | 3.12         | stable         |
| https://docs.python.org/3.11/        | 3.11         | stable         |
| https://docs.python.org/3.10/        | 3.10         | security-fixes |
| https://docs.python.org/3.9/         | 3.9          | security-fixes |
| https://docs.python.org/3.8/         | 3.8          | security-fixes |
| https://docs.python.org/3.7/         | 3.7          | EOL            |
| https://docs.python.org/3.6/         | 3.6          | EOL            |
| https://docs.python.org/3.5/         | 3.5          | EOL            |
| https://docs.python.org/3.4/         | 3.4          | EOL            |
| https://docs.python.org/3.3/         | 3.3          | EOL            |
| https://docs.python.org/3.2/         | 3.2          | EOL            |
| https://docs.python.org/3.1/         | 3.1          | EOL            |
| https://docs.python.org/3.0/         | 3.0          | EOL            |
| https://docs.python.org/2.7/         | 2.7          | EOL            |
| https://docs.python.org/2.6/         | 2.6          | EOL            |
| https://www.python.org/doc/versions/ | All versions |                |
+--------------------------------------+--------------+----------------+
"26.11.2023 17:07:06 - [INFO] - Парсер завершил работу."
```

```
$ python src/main.py whats-new -o pretty
"26.11.2023 17:10:14 - [INFO] - Парсер запущен!"
"26.11.2023 17:10:14 - [INFO] - Аргументы командной строки: Namespace(mode='whats-new', clear_cache=False, output='pretty')"
100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 21/21 [00:02<00:00,  7.01it/s]
+----------------------------------------------+----------------------------+-----------------------------------------------------------------------------------------------------------------+
| Ссылка на статью                             | Заголовок                  | Редактор, Автор                                                                                                 |
+----------------------------------------------+----------------------------+-----------------------------------------------------------------------------------------------------------------+
| https://docs.python.org/3/whatsnew/3.12.html | What’s New In Python 3.12¶ |  Editor Adam Turner                                                                                             |
| https://docs.python.org/3/whatsnew/3.11.html | What’s New In Python 3.11¶ |  Editor Pablo Galindo Salgado                                                                                   |
| https://docs.python.org/3/whatsnew/3.10.html | What’s New In Python 3.10¶ |  Editor Pablo Galindo Salgado                                                                                   |
| https://docs.python.org/3/whatsnew/3.9.html  | What’s New In Python 3.9¶  |  Editor Łukasz Langa                                                                                            |
| https://docs.python.org/3/whatsnew/3.8.html  | What’s New In Python 3.8¶  |  Editor Raymond Hettinger                                                                                       |
| https://docs.python.org/3/whatsnew/3.7.html  | What’s New In Python 3.7¶  |  Editor Elvis Pranskevichus <elvis@magic.io>                                                                    |
| https://docs.python.org/3/whatsnew/3.6.html  | What’s New In Python 3.6¶  |  Editors Elvis Pranskevichus <elvis@magic.io>, Yury Selivanov <yury@magic.io>                                   |
| https://docs.python.org/3/whatsnew/3.5.html  | What’s New In Python 3.5¶  |  Editors Elvis Pranskevichus <elvis@magic.io>, Yury Selivanov <yury@magic.io>                                   |
| https://docs.python.org/3/whatsnew/3.4.html  | What’s New In Python 3.4¶  |  Author R. David Murray <rdmurray@bitdance.com> (Editor)                                                        |
| https://docs.python.org/3/whatsnew/3.3.html  | What’s New In Python 3.3¶  |  PEP 405 - Python Virtual EnvironmentsPEP written by Carl Meyer; implementation by Carl Meyer and Vinay Sajip   |
| https://docs.python.org/3/whatsnew/3.2.html  | What’s New In Python 3.2¶  |  Author Raymond Hettinger                                                                                       |
| https://docs.python.org/3/whatsnew/3.1.html  | What’s New In Python 3.1¶  |  Author Raymond Hettinger                                                                                       |
| https://docs.python.org/3/whatsnew/3.0.html  | What’s New In Python 3.0¶  |  Author Guido van Rossum                                                                                        |
| https://docs.python.org/3/whatsnew/2.7.html  | What’s New in Python 2.7¶  |  Author A.M. Kuchling (amk at amk.ca)                                                                           |
| https://docs.python.org/3/whatsnew/2.6.html  | What’s New in Python 2.6¶  |  Author A.M. Kuchling (amk at amk.ca)                                                                           |
| https://docs.python.org/3/whatsnew/2.5.html  | What’s New in Python 2.5¶  |  Author A.M. Kuchling                                                                                           |
| https://docs.python.org/3/whatsnew/2.4.html  | What’s New in Python 2.4¶  |  Author A.M. Kuchling                                                                                           |
| https://docs.python.org/3/whatsnew/2.3.html  | What’s New in Python 2.3¶  |  Author A.M. Kuchling                                                                                           |
| https://docs.python.org/3/whatsnew/2.2.html  | What’s New in Python 2.2¶  |  Author A.M. Kuchling                                                                                           |
| https://docs.python.org/3/whatsnew/2.1.html  | What’s New in Python 2.1¶  |  Author A.M. Kuchling                                                                                           |
| https://docs.python.org/3/whatsnew/2.0.html  | What’s New in Python 2.0¶  |  Author A.M. Kuchling and Moshe Zadka                                                                           |
+----------------------------------------------+----------------------------+-----------------------------------------------------------------------------------------------------------------+
"26.11.2023 17:10:17 - [INFO] - Парсер завершил работу."
```

```
$ python src/main.py download
"26.11.2023 17:17:30 - [INFO] - Парсер запущен!"
"26.11.2023 17:17:30 - [INFO] - Аргументы командной строки: Namespace(mode='download', clear_cache=False, output=None)"
"26.11.2023 17:17:33 - [INFO] - Архив был загружен и сохранён: C:\Dev\bs4_parser_pep\src\downloads\python-3.12.0-docs-pdf-a4.zip"
"26.11.2023 17:17:33 - [INFO] - Парсер завершил работу."
```