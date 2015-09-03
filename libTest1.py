__author__ = 'Maruthi'


import urllib,urllib2,os,sys
import json,time
import csv,re
import xlsxwriter as xlS
import timeit


#helper functions
def call_api(url,params):
    try:
        data = urllib.urlencode(params)
        url = url + data
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
        url = url + data
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

# Function to crawl based on individual user handle
def instaHandlePost(userId, total=100):
    unique_followerId = []
    unique_userId = []
    unique_mediaId = []
    post_tag = list()
    counter = total
    done1 = False
    handlePosts = list()

    url1 = 'https://api.instagram.com/v1/users/' + userId + '/media/recent/?'
    # WunSG access token
    params1 = {'client_id' : '297d1f6458554ee8b87d0aff6e345d75'}

    cnt1 = 0
    while (done1 == False):


        if cnt1 < 1:
            print 1
            results1 = call_api(url1, params1)
            data1 = results1['data']
        else:
            print 2
            results1 = call_api1(url1)
            data1 = results1['data']
        for item in data1:
            owner_username = item['user']['username']
            owner_id = item['caption']['from']['id']
            post_caption = item['caption']['text']
            post_created = time.strftime("%d/%m/%Y %H:%M", time.localtime(int(item['caption']['created_time'])))
            comment_count = item['comments']['count']
            post_link = item['link']
            like_count = item['likes']['count']
            post_type = item['type']
            media_id = item['id']
            # Due to heights of laziness, We will use the instaComments function here to get the handle mention count here
            # if comment_count > 0:
            data2 = instaComment(media_id)
            print data2
            print len(data2)
            print type(data2)
            handleCount = data2[3]
            post_tags = item['tags']
            for tg in post_tags:
                tg = tg.encode('ascii','ignore')
                post_tag.append(tg)
            handlePost = owner_id, owner_username, post_caption, post_created, comment_count, post_link, like_count, post_type, media_id, post_tag, handleCount
            handlePosts.append(handlePost)

        counter = counter - 1
        # To know the number of post crawled
        # print counter, " API calls left before completion"
        if counter == 0:
                done1 = True
                break
        # The part that moves the pointer to the next set of records

        if counter > 0:
                try:
                    url1 = results1['pagination']['next_url']
                    cnt1 += 1
                    # Setting the intervals between each calls
                    time.sleep(1)

                except:
                    done1 = True
                    break
    return handlePosts

def instaUserInfo(user_id):
        userCount = list()
        url3 = 'https://api.instagram.com/v1/users/' + user_id + '/?'
        params3 = {'client_id' : '56a1bcddc8af46de829258fcd3b5ca47'}
        try:
            results3 = call_api(url3, params3)
            media_count = str(results3['data']['counts']['media'])
            follower_count = str(results3['data']['counts']['followed_by'])
            follow_count = str(results3['data']['counts']['follows'])
            user_name = str(results3['data']['username'])
            useR = media_count, follower_count, follow_count, user_name
            time.sleep(1)
            return useR

        except:
            media_count = "Private Profile"
            follower_count = "Private Profile"
            follow_count = "Private Profile"
            user_name = "Private Profile"
            useR = media_count, follower_count, follow_count, user_name
            time.sleep(1)
            return useR

def instaComment(media_id):
        userComments = list()
        url5 = 'https://api.instagram.com/v1/media/' + media_id + '/comments?'
        params5 = {'client_id' : '56a1bcddc8af46de829258fcd3b5ca47'}

        try:
            results5 = call_api(url5, params5)
            data = results5['data']
            for item in data:
                comment = item['text']
                handleCount = len(re.findall("@[a-zA-Z]+", comment))
                createdTime = time.strftime("%d/%m/%Y %H:%M", time.localtime(int(item['created_time'])))
                userComment = item['from']['username']
                userIdComment = item['from']['id']
                comments = createdTime, userComment, userIdComment, comment, handleCount
                userComments.append(comments)
            return userComments

        except:
            comment = "NIL"
            createdTime = "NIL"
            userComment = "NIL"
            userIdComment = "NIL"
            handleCount = 0
            userComments = createdTime, userComment, userIdComment, comment, handleCount
            return userComments