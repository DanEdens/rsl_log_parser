set log="%userprofile%\AppData\Local\Plarium\PlariumPlay\StandAloneApps\raid\242\log.txt"
tail -f %log% | grep normalization | python main.py
