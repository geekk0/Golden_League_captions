## Golden League captions                       
[переключить на ENG](README.md)

![python version](https://img.shields.io/badge/python-3.8.6-brightgreen)
![languages](https://img.shields.io/github/languages/top/geekk0/Golden_League_captions)
![last-commit](https://img.shields.io/github/last-commit/geekk0/Golden_League_captions)

<br>Скрипты для онлайн трансляций матчей. [Сайт для трансляций](https://github.com/geekk0/Golden_League_site)

##Описание и использование
<br>*files_gen.exe* - Запускается на компе с OBS. Обращается к api сайта и создает 5 текстовых файлов, с данными для формирования онлайн-табло в сцене OBS.
<br>*refresher.py* - Уже запущен на демо-сервере. Генерирует запросы для обновления состояния "Ace/Out"
<br>*ts_files_clean.exe* - Удаляет устаревшие файлы .ts потока.
<br>*db_dumper.py* - Регулярный дамп базы данных.

## Библиотеки

Requests, pyinstaller, json, itertools, time, schedule
