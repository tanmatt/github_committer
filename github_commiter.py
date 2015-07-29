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

def _edit_file(filename):
    with open('times', 'w') as f:
        f.write(str(time.time()))

def do_the_magic(filename):
    try:
        print "1"
        os.system("git pull origin daily")
        time.sleep(5)
        print "2"
        os.system("git checkout daily")
        print "3"
        _edit_file(filename)
        print "4"
        os.system("git add -A")
        print "5"
        os.system("git commit -m \"Daily Commit\" ")
        print "6"
        os.system("git push origin daily")

    except Exception, ex:
        print "Error : %s" % str(ex)



if __name__ == '__main__':
    do_the_magic(FILENAME)
    #_edit_file(FILENAME)
