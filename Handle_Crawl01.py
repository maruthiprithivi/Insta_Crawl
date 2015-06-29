__author__ = 'maruthi'

import urllib,urllib2,os,sys
import json,time
import csv,re
import xlsxwriter as xlS
import timeit


def instaHandlePost(userId, total=100):
    row1 = 0
    col1 = 0
    # row2 = 0
    # col2 = 0
    # row3 = 0
    # col3 = 0
    # row4 = 0
    # col4 = 0
    # row5 = 0
    # col5 = 0
    unique_userId = []
    unique_mediaId = []
    post_tag = list()
    counter = total
    done1 = False

    workbook = xlS.Workbook("output/atb.xlsx")
    worksheet1 = workbook.add_worksheet('Posts')
    # worksheet2 = workbook.add_worksheet('Tags')
    # worksheet3 = workbook.add_worksheet('Followers')
    # worksheet4 = workbook.add_worksheet('User Summary')
    # worksheet5 = workbook.add_worksheet('Likes Info')
    worksheet1.write(row1, col1, "username")
    worksheet1.write(row1, col1 + 1, "user_handle")
    worksheet1.write(row1, col1 + 2, "caption")
    worksheet1.write(row1, col1 + 3, "post_link")
    worksheet1.write(row1, col1 + 4, "created_on")
    worksheet1.write(row1, col1 + 5, "media_id")
    # worksheet1.write(row1, col1 + 6, "image_url")
    worksheet1.write(row1, col1 + 6, "comment_count")
    worksheet1.write(row1, col1 + 7, "like_count")
    worksheet1.write(row1, col1 + 8, "post_type")

    # worksheet2.write(row2, col2, "media_id")
    # worksheet2.write(row2, col2 + 1, "tags")
    # worksheet3.write(row3, col3, "owner_name")
    # worksheet3.write(row3, col3 + 1, "owner_id")
    # worksheet3.write(row3, col3 + 2, "follower_name")
    # worksheet3.write(row3, col3 + 3, "follower_id")
    # worksheet4.write(row4, col4, "owner_name")
    # worksheet4.write(row4, col4 + 1, "owner_id")
    # worksheet4.write(row4, col4 + 2, "media_count")
    # worksheet4.write(row4, col4 + 3, "followed_by_count")
    # worksheet5.write(row5, col5, "owner_name")
    # worksheet5.write(row5, col5 + 1, "owner_id")
    # worksheet5.write(row5, col5 + 2, "media_id")
    # worksheet5.write(row5, col5 + 3, "user_name")
    # worksheet5.write(row5, col5 + 4, "user_id")
    # worksheet5.write(row5, col5 + 5, "relationship_status"

    url1 = 'https://api.instagram.com/v1/users/' + userId + '/media/recent/'
    # WunSG access token
    params1 = {'client_id' : '297d1f6458554ee8b87d0aff6e345d75'}

    cnt1 = 0
    cnt2 = 0
    while (done1 == False):
        if cnt1 < 1:
            startTime = timeit.default_timer()
            # print url1
            results1 = call_api(url1, params1)
            data1 = results1['data']
        else:
            results1 = call_api1(url1)
            data1 = results1['data']
        for item in data1:
            # cnt2 += 1
            # print cnt2
            try:
                owner_username = item['caption']['from']['username']
            except:
                continue
            owner_id = item['caption']['from']['id']
            post_caption = item['caption']['text']
            post_created = time.strftime("%D %H:%M", time.localtime(int(item['caption']['created_time'])))
            comment_count = item['comments']['count']
            post_link = item['link']
            like_count = item['likes']['count']
            post_type = item['type']
            media_id = item['id']
            # if post_type is "image":
            #     media_link = item['images']['standard_resolution']
            # else:
            #     media_link = item['videos']['standard_resolution']



        # To parse the data set into separate segments
        #     owner_username = item['user']['username']
        #     owner_id = item['user']['id']
        #     post_tags = item['tags']
        #     media_link = item['images']['standard_resolution']
        #     for tg in post_tags:
        #         tg = tg.encode('ascii','ignore')
        #         post_tag.append(tg)
        #     try:
        #         post_caption = item['caption']['text']
        #         post_caption = post_caption.encode('ascii','ignore')
        #     except:
        #         post_caption = " "
        #     post_link = item['link']
        #     post_created = time.strftime("%D %H:%M", time.localtime(int(item['created_time'])))
        #     media_id = item['id']
        #     image_url = item['images']['standard_resolution']['url']
        #     # To handle empty values while parsing
        #     try:
        #         comment_counts = item['comments']['count']
        #         # print comment_counts
        #     except:
        #         comment_counts = 0
        #     try:
        #         likes_counts = item['likes']['count']
        #         # print likes_counts
        #     except:
        #         likes_counts = 0
        #     for tag in post_tag:
        #         worksheet2.write(row2 + 1, col2, media_id)
        #         worksheet2.write(row2 + 1, col2 + 1, tag)
        #         row2 += 1
            # row = 0

            worksheet1.write(row1 + 1,col1, owner_username)
            worksheet1.write(row1 + 1,col1 + 1, owner_id)
            worksheet1.write(row1 + 1,col1 + 2, post_caption)
            worksheet1.write(row1 + 1,col1 + 3, post_link)
            worksheet1.write(row1 + 1,col1 + 4, post_created)
            worksheet1.write(row1 + 1,col1 + 5, media_id)
            # worksheet1.write(row1 + 1,col1 + 6, image_url)
            worksheet1.write(row1 + 1,col1 + 6, comment_count)
            worksheet1.write(row1 + 1,col1 + 7, like_count)
            worksheet1.write(row1 + 1,col1 + 8, post_type)
            row1 += 1
            # To print out the stalk log!! LOL!!
            cnt2 += 1
            print str(cnt2) + "x", " Stalking User " + userId + " Completed!!!"

            # # Followers call kicks in!!
            # if owner_id not in unique_userId:
            #     # print owner_id
            #     # To get the unique user handles for crawling out followers
            #     unique_userId.append(owner_id)
            #     # To get the owners summary
            #     followerCount = instaUserInfo(owner_id)
            #     # print type(followerCount)
            #     for counT in followerCount:
            #         media_counT = counT[0]
            #         follower_counT = counT[1]
            #         worksheet4.write(row4 + 1,col4, owner_username)
            #         worksheet4.write(row4 + 1,col4 + 1, owner_id)
            #         worksheet4.write(row4 + 1,col4 + 2, media_counT)
            #         worksheet4.write(row4 + 1,col4 + 3, follower_counT)
            #         row4 += 1
            #
            #     # To get the owners individual followers and their handle
            #     followers = instaFollowers(owner_id)
            #
            #     # print followers
            #     for follower in followers:
            #         # print follower
            #         # The following is a lamo step, integrate it within the write function during the next code iteration (24/06/2015)
            #         follower_name = follower[0]
            #         follower_id = follower[1]
            #         worksheet3.write(row3 + 1,col3, owner_username)
            #         worksheet3.write(row3 + 1,col3 + 1, owner_id)
            #         worksheet3.write(row3 + 1,col3 + 2, follower_name)
            #         worksheet3.write(row3 + 1,col3 + 3, follower_id)
            #         row3 += 1

            # # Likes info kicks in
            # if media_id not in unique_mediaId:
            #     unique_mediaId.append(media_id)
            #     likeInfo = instaLikes(media_id)
            #     print likeInfo
            #     print type(likeInfo)
            #     for likeT in likeInfo:
            #         # print follower
            #         # The following is a lamo step, integrate it within the write function during the next code iteration (24/06/2015)
            #         like_user_name = likeT[0]
            #         like_user_id = likeT[1]
            #         if like_user_id in
            #         worksheet5.write(row5 + 1,col5, owner_username)
            #         worksheet5.write(row5 + 1,col5 + 1, owner_id)
            #         worksheet5.write(row5 + 1,col5 + 2, media_id)
            #         worksheet5.write(row5 + 1,col5 + 3, like_user_name)
            #         worksheet5.write(row5 + 1,col5 + 4, like_user_id)
            #         worksheet5.write(row5 + 1,col5 + 4, "Feature Coming Soon!!")
            #         row5 += 1



        counter = counter - 1
        # To know the number of post crawled
        print counter, " API calls left before completion"
        if counter == 0:
                done1 = True

                print "Crawl Job Finished"
                print url1," is the last pagination link crawled before completing stalking task"
                endTime = timeit.default_timer()
                print startTime
                print endTime
                print "Time taken to stalk on Instagram: ", endTime - startTime
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
                        print "Crawl Job Finished"
                        print url1," is the last pagination link crawled before completing stalking task or quiting because of stupid lame reasons"
    # workbook.close()

def instaFollowers(user_id):
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
                    for item in data2:
                    # To parse the data set into separate segments
                        follower_name = str(item['username'])
                        follower_id = str(item['id'])
                        follower = follower_name, follower_id
                        followers.append(follower)
                    return followers

                    # else:
                    #     results2 = call_api1(url2)
                    #     data2 = results2['data']
                    #     for item in data2:
                    #     # To parse the data set into separate segments
                    #         follower_name = str(item['username'])
                    #         follower_id = str(item['id'])
                    #         follower = follower_name, follower_id
                    #         followers.append(follower)
                    #     return followers

                    try:
                        url2 = results2['pagination']['next_url']

                        cnt4 += 1
                        # Setting the intervals between each calls
                        time.sleep(1)
                    except:
                        done2 = True
                        return url2


def instaUserInfo(user_id):
        cnt5 = 0
        cnt6 = 0
        userCount = list()
        url3 = 'https://api.instagram.com/v1/users/' + user_id + '/'
        params3 = {'client_id' : '56a1bcddc8af46de829258fcd3b5ca47'}

                    # if cnt5 < 1:
                        # print url2
        try:
            results3 = call_api(url3, params3)
            # print results3
            # data3 = results3['data']

            # else:
            #     results2 = call_api1(url2)
            #     data3 = results2['data']
            # for item in data3:
            # To parse the data set into separate segments
            media_count = str(results3['data']['counts']['media'])
            follower_count = str(results3['data']['counts']['followed_by'])
            useR = media_count, follower_count
            userCount.append(useR)
            # print userCount
            # print len(userCount)
            return userCount

        except:
            media_count = "Private Profile"
            follower_count = "Private Profile"
            useR = media_count, follower_count
            userCount.append(useR)
            # print userCount
            # print len(userCount)
            return userCount

                    # try:
                    #     url3 = results2['pagination']['next_url']
                    #     cnt5 += 1
                    #     # Setting the intervals between each calls
                    #     time.sleep(1)
                    # except:
                    #     done3 = True
                    #     return url3

def instaLikes(media_id):
    done4 = False
    cnt7 = 0
    cnt8 = 0
    likeS = list()
    url4 = 'https://api.instagram.com/v1/media/' + media_id + '/likes'
    # WUN SG
    params4 = {'client_id' : '826fe214c1884fcb8bb4a5c65bfb3e29'}
    while (done4 == False):
                    if cnt7 < 1:
                        # print url2
                        results4 = call_api(url4, params4)
                        data4 = results4['data']
                    else:
                        results4 = call_api1(url4)
                        data4 = results4['data']
                    for item in data4:
                    # To parse the data set into separate segments
                        like_userName = str(item['username'])
                        like_id = str(item['id'])
                        likeD = like_userName, like_id
                        likeS.append(likeD)
                    return likeS


                    try:
                        url4 = results2['pagination']['next_url']

                        cnt7 += 1
                        # Setting the intervals between each calls
                        time.sleep(1)
                    except:
                        done4 = True
                        # return url4


#helper functions
def call_api(url,params):
    try:
        data = urllib.urlencode(params)
        url = url + '?' + data
        req = urllib2.Request(url)
        result = json.loads(urllib2.urlopen(req).read())
        return result
    except urllib2.HTTPError:
        print "Error while calling this " + url

def call_api1(url):
    try:
        req = urllib2.Request(url)
        result = json.loads(urllib2.urlopen(req).read())
        return result
    except urllib2.HTTPError:
        print "Error occured while calling this " + url

if __name__ == '__main__':
    try:
        userHandle = sys.argv[1]
    except IndexError:
        print 'Usage: python cr_201.py <user handle> <num of records>'

    if len(sys.argv) >= 3:
        posts = int(sys.argv[2])
        instaHandlePost(userHandle, total=posts)
    else:
        instaHandlePost(userHandle)

