"""
crontab every 1 hour
"""

import os
import time
import wget

FILENAME = 'todays_random_hours.txt'
DOWNLOAD_LINK = 'http://www.zacks.com/portfolios/rank/rank_excel.php?rank=1&reference_id=all'
DOWNLOADED_FILE = "rank_1.xls"

TIME = time.gmtime()
YEAR = time.strftime("%Y", TIME)
MONTH = time.strftime("%m", TIME)
DATE = time.strftime("%d", TIME)
HOUR = int(time.strftime("%H", TIME))
GIT_BRANCH = 'zacks'


def is_downloadable():
    hours = []
    with file(FILENAME) as random_hours:
        hours = random_hours.readlines()
    print "Current Hour: " + HOUR
    print "Downloadable Hours: " + hours

    if str(HOUR) in hours:
        print "File should be downloaded"
    else:
        print "File should not be downloaded. Not the right time."


def download_xls():
    print "Downloading of xls started..."
    # check / create folders
    put_in_dir = "xlsfiles/" + YEAR + "/" + MONTH + "/" + DATE + "/"

    if os.path.isfile("rank_1.xls"):
        os.remove(os.getcwd() + "/rank_1.xls")

    try:
        if is_downloadable():
            if not os.path.isdir(put_in_dir):
                os.makedirs(put_in_dir)
                wget.download(DOWNLOAD_LINK)
                time.sleep(5)
                os.rename(DOWNLOADED_FILE, put_in_dir + DOWNLOADED_FILE)
                time.sleep(2)
                print os.getcwd()
                if os.path.isfile("rank_1.xls"):
                    os.remove("rank_1.xls")
                _upload_to_git()
        print "\rDownloading of xls started...Done"
    except Exception, ex:
        raise ex


def _upload_to_git():
    try:
        print "Uploading to git..."
        # send it back to github
        os.system("git add -A")
        os.system("git commit -m \"Updated with new file on " + str(HOUR) + "\" ")
        os.system("git push origin " + GIT_BRANCH)
        print "\rUploading to git...Done"
    except Exception, ex:
        raise ex


def do_the_magic():
    try:
        print "Doing the magic..."
        # confirm the correct branch
        os.system("git checkout " + GIT_BRANCH)
        download_xls()
    except Exception, ex:
        raise ex


def main():
    """
    main logic
    :return:
    """
    try:
        print "Program execution started...."
        do_the_magic()
        print "Program execution finished..."
    except Exception, ex:
        print "Program execution failed..." + ex


if __name__ == '__main__':
    main()

