__author__ = 'Maruthi'

from libTest1 import *
import sys

if __name__ == '__main__':
    try:
        userHandle = sys.argv[1]
    except IndexError:
        print 'Usage: python testTemplate1.py <user handle> <num of calls>'

    if len(sys.argv) >= 3:
        posts = int(sys.argv[2])
        data1 = instaHandlePost(userHandle, total=posts)
        data2 = instaUserInfo(userHandle)
    else:
        data1 = instaHandlePost(userHandle)
        data2 = instaUserInfo(userHandle)
print "#"*20
print "*"*10
print data1
print "#"*20
print data2
print "*"*10
print "#"*20
