@echo off
:: Raid Shadow Legends PC client Log parser.
:: Created by Dan Edens
:: Requirments:
:: xargs, grep, tail are unix commands included with Git Bash on Windows
:: Python librays:
:: 1. logging  
:: 2. paho.mqtt  


:main
@REM TODO, check requirements or open URL to install
set repodir="%cd%"
pushd %userprofile%\AppData\Local\Plarium\PlariumPlay\StandAloneApps\raid\ && cd 2* || goto:errmsg
Echo Tailing Raid Log file..

:gregstring
set tmp="%1"
IF %tmp% == "" (
        set "Filter=normalization"
    ) ELSE (
        SET "Filter=%1"
    )

tail -f log.txt | grep --line-buffered %Filter% | xargs -I {} python %repodir%\__main__.py {}
popd
goto:eof

:errmsg
echo Location not found..
echo Please download from "https://www.googleadservices.com/pagead/aclk?sa=L&ai=DChcSEwjpqs6igZ7zAhVLa28EHUhUBM4YABABGgJqZg&ae=2&ohost=www.google.com&cid=CAESQOD2pUITy8B_h97U08UnJljXhYgczPBbH_Ye98vku4frJfwXunTcikCNmgRKHmWh2gUAXB6xfJSsroiEGV-LUE4&sig=AOD64_0dmS4L7dWkOWop7soNwGDAAB7eCQ&q=&nis=1&ved=2ahUKEwiMzcGigZ7zAhX_mmoFHQ-2CkkQqyQoAHoECAIQEw&adurl=" 
goto:eof

