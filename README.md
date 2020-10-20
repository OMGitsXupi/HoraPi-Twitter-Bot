# Twitter _hora pi_ bot 
Hello! I'm a bot that likes every *hora pi* tweet and post one as a reminder, too.
- [This is my Twitter account](https://twitter.com/HoraPi__BOT)

### CRONTAB SETUP ###

14 03 * * * python ~/horapiBOT/aviso.py > ~/horapiBOT/aviso.out 2>&1
13 03 * * * python ~/horapiBOT/favs.py > ~/horapiBOT/favs.out 2>&1

16 03 * * * pkill -9 python
17 03 * * * cat ~/horapiBOT/favs.out | mail -s "HORA PI favs log" antoniogs9@hotmail.es
