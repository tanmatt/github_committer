"""
crontab at 23:59:59 everyday
"""

import random
import subprocess
import os

home_dir = subprocess.check_output(["pwd"]).strip()
project_dir = home_dir + '/github_committer/'
os.chdir(project_dir)
FILENAME = project_dir + 'todays_random_hours.txt'


def write_to_file(hour_list):
    with open(FILENAME, 'w') as f:
        for hour in hour_list:
            f.write(str(hour) + "\n")


def get_randoms():
    hours_count = random.randint(1, 7)
    print "hours_count", hours_count
    hours_list = []

    for i in range(hours_count):
        hours_list.append(random.randint(1, 23))

    print "hours_list", hours_list
    write_to_file(hours_list)


if __name__ == '__main__':
    get_randoms()
