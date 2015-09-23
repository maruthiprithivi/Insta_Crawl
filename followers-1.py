__author__ = 'data.team'
__author__ = 'maruthi'

import urllib,urllib2,os,sys
import json,time
import csv,re
import xlsxwriter as xlS


class firstException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class secondException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)


def instaFollowers(user_id, total=100000000):
    # Getting the Handle Summary Info
    userInfo = instaUserInfo(user_id)
    mediaCount = userInfo[0]
    followedByCount = userInfo[1]
    followingCount = userInfo[2]
    userName = userInfo[3]
    counter = total
    counter1 = total
    followers = list()
    row0 = 0
    col0 = 0
    workbook = xlS.Workbook("output1/" + userName + "_handleFollowers.xlsx")
    worksheet0 = workbook.add_worksheet('Followers')
    worksheet0.write(row0, col0, "owner_id")
    worksheet0.write(row0, col0 + 1, "follower_id")
    worksheet0.write(row0, col0 + 2, "follower_name")
    # worksheet0.write(row0, col0 + 3, "media_count")
    # worksheet0.write(row0, col0 + 4, "followed_by_count")
    # worksheet0.write(row0, col0 + 5, "follow_count")
    # worksheet0.write(row0, col0 + 6, "engagement_rate")
    worksheet0.write(row0, col0 + 3, "degree_of_follower")
    done2 = False

    cnt4 = 0
    followers = list()
    url2 = 'https://api.instagram.com/v1/users/' + user_id + '/followed-by'
    # wunsg01-01
    params2 = {'client_id' : '5b77a83635ce4fcbbce5293f2e5314d4'}
    while (done2 == False):
        # print cnt4
        try:
            if cnt4 < 1:
                # print url2
                results2 = call_api(url2, params2)
                data2 = results2['data']
            else:
                results2 = call_api1(url2)
                data2 = results2['data']
        except firstException:
            print "First Except in progress - First Degree"
            # wunsg01-04
            params2 = {'client_id' : '059a16fcf1f4435183abf2c658b329db'}
            results2 = call_api1(url2)
            data2 = results2['data']

        except secondException:
            print "Second Except in progress - First Degree"
            # wunsg01-05
            params2 = {'client_id' : 'def541a4d65c483cad0de027c5cc3d6a'}
            results2 = call_api1(url2)
            data2 = results2['data']

        except:
            print "The crawl of first degree followers broke here - " + url2
            # break
            done2 = True

        # try:
        # print data2
        for item in data2:
        # To parse the data set into separate segments
            follower_name = str(item['username'])
            follower_id = str(item['id'])
            if followers is None:
                followers = follower_id
                print "followers: " + str(len(followers))
            else:
                followers.append(follower_id)
                print "followers: " + str(len(followers))
            # follower = follower_name, follower_id
            # follow1 = instaUserInfo(follower_id)
            # media_count = follow1[0]
            # followed_by_count = follow1[1]
            # follow_count = follow1[2]



            worksheet0.write(row0 + 1, col0, user_id)
            worksheet0.write(row0 + 1, col0 + 1, follower_id)
            worksheet0.write(row0 + 1, col0 + 2, follower_name)
            # worksheet0.write(row0 + 1, col0 + 3, media_count)
            # worksheet0.write(row0 + 1, col0 + 4, followed_by_count)
            # worksheet0.write(row0 + 1, col0 + 5, follow_count)
            # worksheet0.write(row0 + 1, col0 + 6, follow_count)
            worksheet0.write(row0 + 1, col0 + 3, "First Degree")
            row0 += 1
        # except:
        #     print "Something Fishy is Happening MOOOOOOOOO!!"


            counter = counter - 1
            # print counter
            if counter == 0:
                done2 = True
                # print "counter is 0"
            if counter > 0:
                # print "counter not 0"
                try:
                    url2 = results2['pagination']['next_url']
                    cnt4 += 1
                    # print "try"
                    # Setting the intervals between each calls
                    # time.sleep(1)
                except:
                    done2 = True
                    # print "except"
                    print url2

    print "To Arthur - 2nd Degree Starting Now"
    for follower in followers:
        print "2nd Degree"
        url3 = 'https://api.instagram.com/v1/users/' + follower + '/followed-by'
        # wunsg01-02
        params3 = {'client_id' : 'e41e663a0088484da299555491f4323a'}
        cnt5 = 0
        done3 = False
        while (done3 == False):
            if cnt5 < 1:
            # print url2
                try:
                    results3 = call_api(url3, params3)
                    data3 = results3['data']
                    # print data3
                except:
                    print "Failed Moo!!" + follower + "<---The Culprit Moo!!"
                    follower_name1 = str(item['username'])
                    follower_id1 = str(item['id'])
                    # follow1 = instaUserInfo(follower_id1)
                    # media_count1 = follow1[0]
                    # followed_by_count1 = follow1[1]
                    # follow_count1 = follow1[2]
                    worksheet0.write(row0 + 1, col0, follower)
                    worksheet0.write(row0 + 1, col0 + 1, "No Access")
                    worksheet0.write(row0 + 1, col0 + 2, "No Access")
                    # worksheet0.write(row0 + 1, col0 + 3, "No Access")
                    # worksheet0.write(row0 + 1, col0 + 4, "No Access")
                    # worksheet0.write(row0 + 1, col0 + 5, "No Access")
                    # worksheet0.write(row0 + 1, col0 + 6, "No Access")
                    worksheet0.write(row0 + 1, col0 + 3, "Second Degree")
                    row0 += 1
                    break
            else:
                try:
                    results3 = call_api1(url3)
                    data3 = results3['data']
                except firstException:
                    print "First Except in progress - Second Degree"
                    # wunsg02-01
                    params3 = {'client_id' : '05fbaeda2b7648c2a3006a37475a36af'}
                    results3 = call_api1(url3)
                    data3 = results3['data']

                except secondException:
                    print "Second Except in progress - Second Degree"
                    # wunsg02-02
                    params3 = {'client_id' : 'e84d6e63cfba4f0eacb09e9fa5625764'}
                    results3 = call_api1(url3)
                    data3 = results3['data']
                except:
                    print "Failed Moo!!" + url3 + "<---The Culprit Moo!!"
                    done3 = True
            try:
                for item in data3:
                # To parse the data set into separate segments
                    follower_name1 = str(item['username'])
                    follower_id1 = str(item['id'])
                    # follow1 = instaUserInfo(follower_id1)
                    # media_count1 = follow1[0]
                    # followed_by_count1 = follow1[1]
                    # follow_count1 = follow1[2]
                    worksheet0.write(row0 + 1, col0, follower)
                    worksheet0.write(row0 + 1, col0 + 1, follower_id1)
                    worksheet0.write(row0 + 1, col0 + 2, follower_name1)
                    # worksheet0.write(row0 + 1, col0 + 3, media_count1)
                    # worksheet0.write(row0 + 1, col0 + 4, followed_by_count1)
                    # worksheet0.write(row0 + 1, col0 + 5, follow_count1)
                    # worksheet0.write(row0 + 1, col0 + 6, follow_count1)
                    worksheet0.write(row0 + 1, col0 + 3, "Second Degree")
                    row0 += 1
            except:
                print "Failed Mooooooo!!!!"


            # counter1 = counter1 - 1
            if counter1 == 0:
                done3 = True
            if counter1 > 0:
                try:
                    url3 = results3['pagination']['next_url']

                    cnt5 += 1
                    # Setting the intervals between each calls
                    # time.sleep(1)
                except:
                    done3 = True
                    print url3
    workbook.close()

def instaUserInfo(user_id):

        userCount = list()
        url3 = 'https://api.instagram.com/v1/users/' + user_id + '/'
        # wunsg01-03
        params3 = {'client_id' : '739a4990750e4b48bd5a53603e36ce95'}

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
        print url
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
        time.sleep(5)
        data = urllib.urlencode(params)
        url = url + '?' + data
        req = urllib2.Request(url)
        result = json.loads(urllib2.urlopen(req).read())
        return result
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
        time.sleep(5)
        req = urllib2.Request(url)
        result = json.loads(urllib2.urlopen(req).read())
        return result
    except urllib2.URLError:
        print "[Call_API - Time Out Error]: while calling this " +  url

if __name__ == '__main__':
    try:
        userHandle = sys.argv[1]
    except IndexError:
        print 'Usage: python cr_201.py <user handle> <num of records>'

    if len(sys.argv) >= 3:
        posts = int(sys.argv[2])
        instaFollowers(userHandle, total=posts)
        print "posts: ", posts
    else:
        instaFollowers(userHandle)