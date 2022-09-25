# Remainder
This is a simple script to remind the birthday and work anniversary of the team members

### Steps to install

```
pip install requirements.txt
```

### Schedule the cron job 

Schedule Everyday at 8:00 AM for the script Birtday_wish.py

```
0 8 * * * python3 /path/to/script/Remainder.py >/tmp/stdout.log 2>/tmp/stderr.log
``` 