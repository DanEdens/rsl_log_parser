:: Raid Shadow Legends PC client Log parser.
:: Created by Dan Edens
:: Requirments:
:: xargs, grep, tail are unix commands included with Git Bash on Windows
:: Python librays:
:: logging - paho.mqtt

@echo off

:main
set repodir="%cd%"
pushd %userprofile%\AppData\Local\Plarium\PlariumPlay\StandAloneApps\raid\ && cd 2* || echo Locaton not found & echo Please download from "https://www.googleadservices.com/pagead/aclk?sa=L&ai=DChcSEwjpqs6igZ7zAhVLa28EHUhUBM4YABABGgJqZg&ae=2&ohost=www.google.com&cid=CAESQOD2pUITy8B_h97U08UnJljXhYgczPBbH_Ye98vku4frJfwXunTcikCNmgRKHmWh2gUAXB6xfJSsroiEGV-LUE4&sig=AOD64_0dmS4L7dWkOWop7soNwGDAAB7eCQ&q=&nis=1&ved=2ahUKEwiMzcGigZ7zAhX_mmoFHQ-2CkkQqyQoAHoECAIQEw&adurl=" & goto:eof
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

