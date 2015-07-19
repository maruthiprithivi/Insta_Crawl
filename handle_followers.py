__author__ = 'maruthi'

import urllib,urllib2,os,sys
import json,time
import csv,re
import xlsxwriter as xlS





def instaFollowers(user_id):
    # Getting the Handle Summary Info
    userInfo = instaUserInfo(user_id)
    mediaCount = userInfo[0]
    followedByCount = userInfo[1]
    followingCount = userInfo[2]
    userName = userInfo[3]

    row0 = 0
    col0 = 0
    workbook = xlS.Workbook("output/" + userName + "_handleFollowers.xlsx")
    worksheet0 = workbook.add_worksheet('Followers')
    worksheet0.write(row0, col0, "owner_id")
    worksheet0.write(row0, col0 + 1, "follower_id")
    worksheet0.write(row0, col0 + 2, "follower_name")
    worksheet0.write(row0, col0 + 3, "media_count")
    worksheet0.write(row0, col0 + 4, "followed_by_count")
    worksheet0.write(row0, col0 + 5, "follow_count")
    done2 = False
    cnt3 = 0
    cnt4 = 0
    followers = list()
    url2 = 'https://api.instagram.com/v1/users/' + user_id + '/followed-by'
    # WUN SG
    params2 = {'client_id' : '826fe214c1884fcb8bb4a5c65bfb3e29'}
    while (done2 == False):
                    if cnt4 < 1:
                        # print url2
                        results2 = call_api(url2, params2)
                        data2 = results2['data']
                    else:
                        results2 = call_api1(url2)
                        data2 = results2['data']

                    try:
                        for item in data2:
                        # To parse the data set into separate segments
                            follower_name = str(item['username'])
                            follower_id = str(item['id'])
                            # follower = follower_name, follower_id
                            follow1 = instaUserInfo(follower_id)
                            media_count = follow1[0]
                            followed_by_count = follow1[1]
                            follow_count = follow1[2]

                            worksheet0.write(row0, col0, user_id)
                            worksheet0.write(row0 + 1, col0 + 1, follower_id)
                            worksheet0.write(row0 + 1, col0 + 2, follower_name)
                            worksheet0.write(row0 + 1, col0 + 3, media_count)
                            worksheet0.write(row0 + 1, col0 + 4, followed_by_count)
                            worksheet0.write(row0 + 1, col0 + 5, follow_count)
                            row0 += 1
                    except:
                        print data2


                    try:
                        url2 = results2['pagination']['next_url']

                        cnt4 += 1
                        # Setting the intervals between each calls
                        time.sleep(1)
                    except:
                        done2 = True
                        return url2

def instaUserInfo(user_id):

        userCount = list()
        url3 = 'https://api.instagram.com/v1/users/' + user_id + '/'
        params3 = {'client_id' : '56a1bcddc8af46de829258fcd3b5ca47'}

                    # if cnt5 < 1:
                        # print url2
        results3 = call_api(url3, params3)
        # print results3
        try:
            results3 = call_api(url3, params3)
            # print results3
            media_count = str(results3['data']['counts']['media'])
            follower_count = str(results3['data']['counts']['followed_by'])
            follow_count = str(results3['data']['counts']['follows'])
            user_name = str(results3['data']['username'])
            useR = media_count, follower_count, follow_count, user_name
            # userCount.append(useR)
            return useR

        except:
            media_count = "Private Profile"
            follower_count = "Private Profile"
            follow_count = "Private Profile"
            user_name = "Private Profile"
            useR = media_count, follower_count, follow_count, user_name
            return useR

#helper functions
def call_api(url,params):
    try:
        data = urllib.urlencode(params)
        url = url + '?' + data
        req = urllib2.Request(url)
        result = json.loads(urllib2.urlopen(req).read())
        return result
        # print result
    except urllib2.HTTPError:
        # result = "Private Profile", "Private Profile", "Private Profile" , "Private Profile"
        # return result
        print "[Call_API - Error]: while calling this " + url

        # worksheet99.write(row99, col99, timeit.default_timer())
    except urllib2.URLError:
        print "[Call_API - Time Out Error]: while calling this " +  url

def call_api1(url):
    try:
        req = urllib2.Request(url)
        result = json.loads(urllib2.urlopen(req).read())
        return result
    except urllib2.HTTPError:
        print "[Call_API - Error]: while calling this " + url

    except urllib2.URLError:
        print "[Call_API - Time Out Error]: while calling this " +  url

if __name__ == '__main__':
    try:
        userHandle = sys.argv[1]
    except IndexError:
        print 'Usage: python cr_201.py <user handle> <num of records>'

    if len(sys.argv) >= 3:
        posts = int(sys.argv[2])
        instaFollowers(userHandle)
    else:
        instaFollowers(userHandle)