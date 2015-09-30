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
    except urllib2.HTTPError:
        print "[Call_API - Error]: while calling this " + url

        # worksheet99.write(row99, col99, timeit.default_timer())
    except urllib2.URLError:
        time.sleep(1)
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
        time.sleep(1)
        req = urllib2.Request(url)
        result = json.loads(urllib2.urlopen(req).read())
        return result
    except urllib2.URLError:
        print "[Call_API - Time Out Error]: while calling this " +  url

# Function to crawl based on individual user handle
def instaHandlePost(userId, total=10000000):
    unique_followerId = []
    unique_userId = []
    unique_mediaId = []
    # post_tag = list()
    counter = total
    done1 = False
    handlePosts = list()
    con = open('token1_1.txt', 'r')
    for tokens in con:
        token1 = tokens.split(',')
        tokenLen = len(token1) - 1
    tokenNo1 = 0
    cnt1 = 0
    url1 = 'https://api.instagram.com/v1/users/' + userId + '/media/recent/?'
    # Set the parameter here so that whenever the job starts it starts with the first key as its default key
    params1 = {'client_id' :token1[tokenNo1]}
    while (done1 == False):
        results1 = call_api(url1, params1)
        data1 = results1['data']
        # expected meta responses : '200' is all good, '429' is limit exceeded, '400' Instagram is blocking us as it suspects our calls are suspicious or basically they hate you!!!
        responsE = results1['meta']['code']


        if cnt1 < 1:
            try:
                params1 = {'client_id' :token1[tokenNo1]}
                results1 = call_api(url1, params1)
                # print results1
                data1 = results1['data']
                # trigger = results1['meta']['code']
            except:
                if tokenNo1 <=tokenLen:
                    tokenNo1 += 1
                else:
                    tokenNo1 = 0
                # print type(token1[tokenNo1])
                params1 = {'client_id' :token1[tokenNo1]}
                results1 = call_api(url1, params1)
                # print results1
                data1 = results1['data']
                # trigger = results1['meta']['code']
        else:
            try:
                idLoc1 = url1.find("&")
                link1 = url1[:idLoc1+11]
                url1 = link1 + str(token1[tokenNo1])
                results1 = call_api1(url1)
                data1 = results1['data']
                # trigger = results1['meta']['code']
            except:
                if tokenNo1 <=tokenLen:
                    tokenNo1 += 1
                else:
                    tokenNo1 = 0
                idLoc1 = url1.find("&")
                link1 = url1[:idLoc1+11]
                url1 = link1 + str(token1[tokenNo1])
                results1 = call_api1(url1)
                data1 = results1['data']
                # trigger = results1['meta']['code']
        for item in data1:
            owner_username = item['user']['username']
            try:
                owner_id = item['caption']['from']['id']
            except:
                owner_id = owner_id
            try:
                post_caption = item['caption']['text']
            except:
                post_caption = " "
            post_created = time.strftime("%d/%m/%Y %H:%M", time.localtime(int(item['caption']['created_time'])))
            comment_count = item['comments']['count']
            post_link = item['link']
            like_count = item['likes']['count']
            post_type = item['type']
            media_id = item['id']
            try:
                media_link = item['images']['standard_resolution']['url']
            except ValueError:
                media_link = item['videos']['standard_resolution']['url']
            except:
                media_link = "No Links"
            # Due to heights of laziness, We will use the instaComments function here to get the handle mention count here
            # if comment_count > 0:
            # data2 = instaComment(media_id)
            # print data2
            # print len(data2)
            # print type(data2)
            # handleCount = data2[4]
            # handleCount = 1
            post_tags = item['tags']
            post_tag = list()
            for tg in post_tags:
                tg = tg.encode('ascii','ignore')
                post_tag.append(tg)
            # handlePost = owner_id, owner_username, post_caption, post_created, comment_count, post_link, like_count, post_type, media_id, post_tag, handleCount, media_link
            handlePost = owner_id, owner_username, post_caption, post_created, comment_count, post_link, like_count, post_type, media_id, post_tag, media_link
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
                    # time.sleep(1)

                except:
                    done1 = True
                    break
    return handlePosts

def instaUserInfo(user_id):
        con = open('token1_1.txt', 'r')
        for tokens in con:
            token2 = tokens.split(',')
            tokenLen = len(token2) - 1
        tokenNo2 = 0
        userCount = list()
        url3 = 'https://api.instagram.com/v1/users/' + user_id + '/?'

        try:
            params3 = {'client_id' :token2[tokenNo2]}
            results3 = call_api(url3, params3)
            trigger = results3['meta']['code']
            if trigger == 429:
                tokenNo2 += 1
                params3 = {'client_id' :token2[tokenNo2]}
                results3 = call_api(url3, params3)
            media_count = str(results3['data']['counts']['media'])
            follower_count = str(results3['data']['counts']['followed_by'])
            follow_count = str(results3['data']['counts']['follows'])
            user_name = str(results3['data']['username'])
            useR = media_count, follower_count, follow_count, user_name
            # time.sleep(1)
            return useR

        except:
            media_count = "Private Profile"
            follower_count = "Private Profile"
            follow_count = "Private Profile"
            user_name = "Private Profile"
            useR = media_count, follower_count, follow_count, user_name
            # time.sleep(1)
            return useR

def instaComment(media_id):
        con = open('token1_1.txt', 'r')
        for tokens in con:
            token3 = tokens.split(',')
            tokenLen = len(token3) - 1
        tokenNo3 = 0
        userComments = list()
        url5 = 'https://api.instagram.com/v1/media/' + media_id + '/comments?'

        try:
            params5 = {'client_id' :token3[tokenNo3]}
            results5 = call_api(url5, params5)
            trigger = results5['meta']['code']
            if trigger == 429:
                tokenNo3 += 1
                params5 = {'client_id' :token3[tokenNo3]}
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