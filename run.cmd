:: Raid Shadow Legends PC clien Log parser.
:: Created by Dan Edens
:: Requirments:
:: xargs, grep, tail are unix commands included with Git Bash on Windows
:: Python librays:
:: logging - paho.mqtt

@echo off

:main
set repodir="%cd%"
pushd %userprofile%\AppData\Local\Plarium\PlariumPlay\StandAloneApps\raid\
cd 2*
Echo Tailing Raid Log file..
REM Only reacts to lines including text: "normalization"
tail -f log.txt | grep --line-buffered normalization | xargs -I {} python %repodir%\__main__.py {}
popd
goto:eof


:hardcoded
:: (Legacy) Instead of the file itself, it's easier to glob walk into the current version's folder,
:: from before i realized they made a whole folder per version instead of just using git.. 
set log="%userprofile%\AppData\Local\Plarium\PlariumPlay\StandAloneApps\raid\250\log.txt
tail -f %log% | grep --line-buffered normalization | xargs -I {} python __main__.py {}
goto:eof

