@echo off
@REM set log="%userprofile%\AppData\Local\Plarium\PlariumPlay\StandAloneApps\raid\245\log.txt"
pushd %userprofile%\AppData\Local\Plarium\PlariumPlay\StandAloneApps\raid\
cd 2*
Echo Tailing Raid Log file..
@REM instead of the file itself, it's easy to glob walk into the current version's folder..
@REM tail -f %log% | grep --line-buffered normalization | xargs -I {} python main.py {}
tail -f log.txt | grep --line-buffered normalization | xargs -I {} python main.py {}
popd
