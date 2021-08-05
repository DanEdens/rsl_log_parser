@echo off
set log="%userprofile%\AppData\Local\Plarium\PlariumPlay\StandAloneApps\raid\245\log.txt"
Echo Tailing Raid Log file..
tail -f %log% | grep --line-buffered normalization | xargs -I {} python main.py {}
