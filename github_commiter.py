__author__ = 'tthakur'
"""
Program that will
 run on a server
 add timestamp to a file
 git add
 git commit
 git push (SSH key authentication)
"""
import sys
import os
import time

FILENAME = 'times'
LOGFILE = 'log'
TIME = str(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))

def _edit_file(filename):
    with open('times', 'a') as f:
        f.write(TIME)


def _flush_log( msg ):
    with open(LOGFILE, 'a') as f:
        f.write(msg)


def do_the_magic(filename):
    try:
        os.system("git pull origin daily")
        time.sleep(5)
        os.system("git checkout daily")
        _edit_file(filename)
        os.system("git add -A")
        os.system("git commit -m \"Daily Commit\" ")
        os.system("git push origin daily")
        _flush_log(TIME + ': Success\n')
    except Exception, ex:
        _flush_log(TIME + ': Failure = ' + str(ex))



if __name__ == '__main__':
    do_the_magic(FILENAME)
    