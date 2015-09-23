__author__ = 'Maruthi'

from libTest1 import *
from storageLib01 import *
import sys

# useR = media_count, follower_count, follow_count, user_name

if __name__ == '__main__':
    try:
        userHandle = sys.argv[1]
    except IndexError:
        print 'Usage: python testTemplate1.py <user handle> <num of calls>'

    if len(sys.argv) >= 3:
        posts = int(sys.argv[2])
        data1 = instaHandlePost(userHandle, total=posts)
        data2 = instaUserInfo(userHandle)
        userName = data2[3]
        handleWriter(data1,userName)
    else:
        data1 = instaHandlePost(userHandle)
        data2 = instaUserInfo(userHandle)
        userName = data2[3]
        handleWriter(data1,userName)

