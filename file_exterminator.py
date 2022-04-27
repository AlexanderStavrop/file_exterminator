import os
import time
import datetime

# Path of folder you want to check
path = ''

# Max days a file can stay untouched in the folder
delete_after = 20


today_time = datetime.datetime.today()

for curr_file in os.listdir(path):
    if curr_file != "desktop.ini":                                  # Needed for windows filesystem
        os.chdir(path)
        f_date = datetime.datetime.strptime(time.ctime(os.path.getmtime(curr_file)), "%a %b %d %H:%M:%S %Y")
        dif_time = f_date + datetime.timedelta(days=delete_after)
        if today_time > dif_time:
            os.remove(curr_file)
