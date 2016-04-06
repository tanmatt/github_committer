"""
crontab every 1 hour
"""

import os
import time
import subprocess
import wget

FILENAME = 'todays_random_hours.txt'
LOGFILE = 'events.log'
DOWNLOAD_LINK = 'http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.csv'
DOWNLOADED_FILE = DOWNLOAD_LINK.split("/")[-1]

TIME = time.gmtime()
YEAR = time.strftime("%Y", TIME)
MONTH = time.strftime("%m", TIME)
DATE = time.strftime("%d", TIME)
HOUR = int(time.strftime("%H", TIME))
GIT_BRANCH = 'earthquake'

log_message = "\n" + str(time.strftime("%Y-%m-%d:", TIME)) + "\t"


def _flush_log():
    with open(LOGFILE, 'a') as f:
        f.write(log_message)


def download_csv():
    # check / create folders
    project_dir = subprocess.check_output(["pwd"]).strip()
    put_in_dir = project_dir + "/csvfiles/" + YEAR + "/" + MONTH + "/" + DATE + "/"
    global log_message
    if not os.path.isdir(put_in_dir):
        os.makedirs(put_in_dir)
        print wget.download(DOWNLOAD_LINK)
        time.sleep(5)
        os.rename(project_dir + "/" + DOWNLOADED_FILE, put_in_dir + DOWNLOADED_FILE)
        log_message += "Downloaded file for today\t"
    else:
        log_message += "Already downloaded the file for today\t"


def do_the_magic():
    try:
        global log_message
        # confirm the correct branch
        os.system("git checkout " + GIT_BRANCH)
        download_csv()

        # send it back to github
        os.system("git add -A")
        os.system("git commit -m \"Updated with new file on " + str(HOUR) + "\" ")
        os.system("git push origin " + GIT_BRANCH)
    except Exception, ex:
        log_message += str(ex) + "\t"


def main():
    """
    main logic
    :return:
    """
    try:
        global log_message
        hours = []
        with open(FILENAME, 'r') as f:
            hours.extend(f.readlines())

        hours_today = []
        for hour in hours:
            hours_today.append(int(hour.strip()))

        if HOUR in hours_today:
            log_message += "File should be downloaded. HOUR= " + str(HOUR) + "\t"
            do_the_magic()
        else:
            log_message += "Not a good time to download. HOUR= " + str(HOUR) + "\t"

        _flush_log()
    except Exception, ex:
        log_message += str(ex) + "\t"
        _flush_log()

if __name__ == '__main__':
    main()

