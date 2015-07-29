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
    fd = os.open(filename)
    os.write(fd, str(time.time()))
    os.close(fd)

def do_the_magic(filename):
    try:
        print "1"
        os.system("git pull")
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
