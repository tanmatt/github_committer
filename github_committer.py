"""
crontab every 1 hour
"""

import os
import time
import wget
import sys

FILENAME = 'todays_random_hours.txt'
DOWNLOAD_LINK = 'http://www.zacks.com/portfolios/rank/rank_excel.php?rank=1&reference_id=all'
DOWNLOADED_FILE = "rank_1.xls"

TIME = time.localtime()
YEAR = time.strftime("%Y", TIME)
MONTH = time.strftime("%m", TIME)
DATE = time.strftime("%d", TIME)
HOUR = str(int(time.strftime("%H", TIME)))
GIT_BRANCH = 'zacks'


def is_downloadable():
    # return true of --force parameter is passed from command line
    if len(sys.argv) > 1 and sys.argv[1] == "--force":
        print "\nForcing the file download because of --force parameter"
        return True

    # else check if the current hour matches with the file content
    downloadable_hours = []
    with file(FILENAME, "r") as random_hours:
        hours = random_hours.readlines()
        for hour in hours:
            downloadable_hours.append(hour.strip())

    print "Current Hour: " + HOUR
    print "Downloadable Hours: " + str(downloadable_hours)

    if HOUR in downloadable_hours:
        print "File should be downloaded"
        return True
    else:
        print "File should not be downloaded. Not the right time."
        return False


def download_xls():
    print "Downloading of xls started..."
    # check / create folders
    put_in_dir = "xlsfiles/" + YEAR + "/" + MONTH + "/" + DATE + "/"

    if os.path.isfile("rank_1.xls"):
        os.remove(os.getcwd() + "/rank_1.xls")

    try:
        if is_downloadable():
            # make dir if not present
            if not os.path.isdir(put_in_dir):
                os.makedirs(put_in_dir)

            print "Downloading file now..."
            wget.download(DOWNLOAD_LINK)
            print "\rDownloading file now...Done"
            time.sleep(5)
            os.rename(DOWNLOADED_FILE, put_in_dir + DOWNLOADED_FILE)
            time.sleep(2)
            print os.getcwd()
            # remove duplicate file from project root
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
        os.system("git commit -m \"Updated with new file on " + HOUR + "\" ")
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
        print "Program execution failed..." + str(ex)


if __name__ == '__main__':
    main()

