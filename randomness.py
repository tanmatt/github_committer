"""
crontab at 23:59:59 everyday
"""

import random
import subprocess
import os
import time

home_dir = subprocess.check_output(["pwd"]).strip()
project_dir = home_dir + '/github_committer/'
os.chdir(project_dir)
FILENAME = project_dir + 'todays_random_hours.txt'
LOGFILE = project_dir + 'events.log'

TIME = time.gmtime()
log_message = "\n" + str(time.strftime("%Y-%m-%d:", TIME)) + "\t"


def _flush_log():
    with open(LOGFILE, 'a') as f:
        f.write(log_message)


def write_to_file(hour_list):
    with open(FILENAME, 'w') as f:
        for hour in hour_list:
            f.write(str(hour) + "\n")


def get_randoms():
    hours_count = random.randint(1, 7)
    print "hours_count", hours_count
    global log_message
    log_message += str(hours_count) + " commits will be done today\t"
    hours_list = []

    for i in range(hours_count):
        hours_list.append(random.randint(1, 23))

    print "hours_list", hours_list
    write_to_file(hours_list)
    log_message += "And it will run on hours = " + str(hours_list)


if __name__ == '__main__':
    get_randoms()
