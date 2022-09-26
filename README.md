## Golden League captions                       
[switch to RU](README.rus.md)

![python version](https://img.shields.io/badge/python-3.8.6-brightgreen)
![languages](https://img.shields.io/github/languages/top/geekk0/Golden_League_captions)
![last-commit](https://img.shields.io/github/last-commit/geekk0/Golden_League_captions)

<br>Scripts for matches live-streaming. [Site for online-streaming]()

##Description and usage
<br>*files_gen.exe* - Starts on pc with OBS. Script calls site api сайта and creates 5 text files, with data for scoreboard.
<br>*refresher.py* - Already running on demo-server. Generate requests for "Ace/Out" state refreshing.
<br>*ts_files_clean.exe* - Removing outdated stream .ts files.
<br>*db_dumper.py* - Scheduled database dump.

## Libs

Requests, pyinstaller, json, itertools, time, schedule
