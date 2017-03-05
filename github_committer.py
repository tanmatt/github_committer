"""
crontab every 1 hour
"""

import os
import time
import wget

FILENAME = 'todays_random_hours.txt'
LOGFILE = 'events.log'
DOWNLOAD_LINK = 'http://www.zacks.com/portfolios/rank/rank_excel.php?rank=1&reference_id=all'
DOWNLOADED_FILE = "rank_1.xls"

TIME = time.gmtime()
YEAR = time.strftime("%Y", TIME)
MONTH = time.strftime("%m", TIME)
DATE = time.strftime("%d", TIME)
HOUR = int(time.strftime("%H", TIME))
GIT_BRANCH = 'zacks'

log_message = "\n" + str(time.strftime("%Y-%m-%d:", TIME)) + "\t"


def _flush_log():
    with open(LOGFILE, 'a') as f:
        f.write(log_message)


def download_xls():
    # check / create folders
    put_in_dir = "xlsfiles/" + YEAR + "/" + MONTH + "/" + DATE + "/"
    print put_in_dir
    global log_message
    if not os.path.isdir(put_in_dir):
        os.makedirs(put_in_dir)

    print "Tanmay: pwd: " + os.getcwd()
    if os.path.isfile("rank_1.xls"):
        print "Tanmay: inside"
        os.remove("rank_1.xls")
    else:
        print "Tanmay: outside"

    try:
        wget.download(DOWNLOAD_LINK)
        time.sleep(5)
        os.rename(DOWNLOADED_FILE, put_in_dir + DOWNLOADED_FILE)
        time.sleep(2)
        print os.getcwd()
        if os.path.isfile("rank_1.xls"):
            os.remove("rank_1.xls")
        log_message += "Downloaded file for today\t"
    except Exception, ex:
        log_message += "Error moving the file: " + str(ex)


def do_the_magic():
    try:
        global log_message
        # confirm the correct branch
        os.system("git checkout " + GIT_BRANCH)
        download_xls()

        # send it back to github
        os.system("git add -A")
        os.system("git commit -m \"Updated with new file on " + str(HOUR) + "\" ")
        os.system("git push origin " + GIT_BRANCH)
    except Exception, ex:
        log_message += "Doing magic:" + str(ex) + "\t"


def main():
    """
    main logic
    :return:
    """
    try:
        global log_message
        log_message += "File should be downloaded. HOUR= " + str(HOUR) + "\t"
        do_the_magic()
        _flush_log()
    except Exception, ex:
        log_message += str(ex) + "\t"
        _flush_log()

if __name__ == '__main__':
    main()

