__author__ = 'maruthi'

import urllib,urllib2,os,sys
import json,time
import csv,re
import xlsxwriter as xlS


def instaPost(tag, total=10000):
    row1 = 0
    col1 = 0
    row2 = 0
    col2 = 0
    row3 = 0
    col3 = 0
    unique_userId = []
    post_tag = list()
    counter = total
    done1 = False
    workbook = xlS.Workbook("output/riplky.xlsx")
    worksheet1 = workbook.add_worksheet('Posts')
    worksheet2 = workbook.add_worksheet('Tags')
    worksheet3 = workbook.add_worksheet('Followers')
    worksheet1.write(row1, col1, "username")
    worksheet1.write(row1, col1 + 1, "user_handle")
    worksheet1.write(row1, col1 + 2, "caption")
    worksheet1.write(row1, col1 + 3, "post_link")
    worksheet1.write(row1, col1 + 4, "created_on")
    worksheet1.write(row1, col1 + 5, "media_id")
    worksheet1.write(row1, col1 + 6, "image_url")
    worksheet1.write(row1, col1 + 7, "comment_count")
    worksheet1.write(row1, col1 + 8, "like_count")
    worksheet2.write(row2, col2, "media_id")
    worksheet2.write(row2, col2 + 1, "tags")
    worksheet3.write(row3, col3, "owner_name")
    worksheet3.write(row3, col3 + 1, "owner_id")
    worksheet3.write(row3, col3 + 2, "follower_name")
    worksheet3.write(row3, col3 + 3, "follower_id")

    url1 = 'https://api.instagram.com/v1/tags/' + tag + '/media/recent'
    # WunSG access token
    params1 = {'client_id' : '297d1f6458554ee8b87d0aff6e345d75'}
    
    cnt1 = 0
    cnt2 = 0
    while (done1 == False):
        print url1
        results1 = call_api(url1, params1)
        data1 = results1['data']
        for item in data1:
        # To parse the data set into separate segments
            owner_username = item['user']['username']
            owner_id = item['user']['id']
        # To get the unique user handles for crawling out followers
        #     for iDs in owner_id:


            post_tags = item['tags']
            for tg in post_tags:
                tg = tg.encode('ascii','ignore')
                post_tag.append(tg)
            post_caption = item['caption']['text']
            post_caption = post_caption.encode('ascii','ignore')
            post_link = item['link']
            post_created = time.strftime("%D %H:%M", time.localtime(int(item['created_time'])))
            media_id = item['id']
            image_url = item['images']['standard_resolution']['url']
            # To handle empty values while parsing
            try:
                comment_counts = item['comments']['count']
                # print comment_counts
            except:
                comment_counts = 0
            try:
                likes_counts = item['likes']['count']
                # print likes_counts
            except:
                likes_counts = 0
            # out_data = str(owner_username), str(owner_id), post_tag, str(post_caption), str(post_link), str(post_created), str(media_id), str(image_url),comment_counts, likes_counts
            for tag in post_tag:
                worksheet2.write(row2 + 1, col2, media_id)
                worksheet2.write(row2 + 1, col2 + 1, tag)
                row2 += 1
            row = 0
            worksheet1.write(row1 + 1,col1, owner_username)
            worksheet1.write(row1 + 1,col1 + 1, owner_id)
            worksheet1.write(row1 + 1,col1 + 2, post_caption)
            worksheet1.write(row1 + 1,col1 + 3, post_link)
            worksheet1.write(row1 + 1,col1 + 4, post_created)
            worksheet1.write(row1 + 1,col1 + 5, media_id)
            worksheet1.write(row1 + 1,col1 + 6, image_url)
            worksheet1.write(row1 + 1,col1 + 7, comment_counts)
            worksheet1.write(row1 + 1,col1 + 8, likes_counts)
            row1 += 1

            if owner_id not in unique_userId:
                print owner_id
                unique_userId.append(owner_id)

                followers = instaFollowers(owner_id)
                print followers
                for follower in followers:
                    # print follower
                    follower_name = follower[0]
                    follower_id = follower[0]
                    worksheet3.write(row3 + 1,col3, owner_username)
                    worksheet3.write(row3 + 1,col3 + 1, owner_id)
                    worksheet3.write(row3 + 1,col3 + 2, follower_name)
                    worksheet3.write(row3 + 1,col3 + 3, follower_id)
                    row3 += 1
                """
                cnt3 = 0
                cnt4 = 0
                # follower_name = list()
                # follower_id = list()
                done2 = False
                url2 = 'https://api.instagram.com/v1/users/' + owner_id + '/followed-by'
                # Wei Tuck Client ID
                params2 = {'client_id' : '9d2997dba5f942c4824c98d885781f74'}
                while (done2 == False):
                    if cnt4 < 1:
                        # print url2
                        results2 = call_api(url2, params2)
                        data2 = results2['data']
                        for item in data2:
                        # To parse the data set into separate segments
                            follower_name = str(item['username'])
                            follower_id = str(item['id'])
                            # print follower_name, follower_id
                            cnt3 += 1
                            # print cnt
                            worksheet3.write(row3 + 1,col3, owner_username)
                            worksheet3.write(row3 + 1,col3 + 1, owner_id)
                            worksheet3.write(row3 + 1,col3 + 2, follower_name)
                            worksheet3.write(row3 + 1,col3 + 3, follower_id)
                            row3 += 1
                    else:
                        results2 = call_api1(url2)
                        data2 = results2['data']
                        for item in data2:
                        # To parse the data set into separate segments
                        #     print (str(item['username']))
                        #     print (str(item['id']))
                            follower_name = str(item['username'])
                            follower_id = str(item['id'])
                            # print follower_name, follower_id
                            cnt3 += 1
                            worksheet3.write(row3 + 1,col3, owner_username)
                            worksheet3.write(row3 + 1,col3 + 1, owner_id)
                            worksheet3.write(row3 + 1,col3 + 2, follower_name)
                            worksheet3.write(row3 + 1,col3 + 3, follower_id)
                            row3 += 1
                    try:
                        url2 = results2['pagination']['next_url']
                        # print url2
                        cnt4 += 1
                        # Setting the intervals between each calls
                        time.sleep(1)
                    except:
                        done2 = True
                    """

            # print out_data
            counter = counter - 1
            if counter == 0:
                    done1 = True
                    break
            # The part that moves the pointer to the next set of records
            if counter > 0:
                    try:
                            url1 = results1['pagination']['next_url']
                            # Setting the intervals between each calls
                            time.sleep(1)

                    except:
                            done1 = True
    workbook.close()

def instaFollowers(user_id):
    done2 = False
    cnt3 = 0
    cnt4 = 0
    followers = list()
    url2 = 'https://api.instagram.com/v1/users/' + user_id + '/followed-by'
    # Wei Tuck Client ID
    params2 = {'client_id' : '9d2997dba5f942c4824c98d885781f74'}
    while (done2 == False):
                    if cnt4 < 1:
                        # print url2
                        results2 = call_api(url2, params2)
                        data2 = results2['data']
                        for item in data2:
                        # To parse the data set into separate segments
                            follower_name = str(item['username'])
                            follower_id = str(item['id'])
                            # followers.append((follower_name,follower_id))
                            follower = follower_name, follower_id
                            # print follower
                            followers.append(follower)
                        # print followers
                        return followers

                            # print follower_name, follower_id
                            # cnt3 += 1
                            # print cnt
                            # worksheet3.write(row3 + 1,col3, owner_username)
                            # worksheet3.write(row3 + 1,col3 + 1, owner_id)
                            # worksheet3.write(row3 + 1,col3 + 2, follower_name)
                            # worksheet3.write(row3 + 1,col3 + 3, follower_id)
                            # row3 += 1
                    else:
                        results2 = call_api1(url2)
                        data2 = results2['data']
                        for item in data2:
                        # To parse the data set into separate segments
                        #     print (str(item['username']))
                        #     print (str(item['id']))
                            follower_name = str(item['username'])
                            follower_id = str(item['id'])
                            # followers.append((follower_name,follower_id))
                            follower = follower_name, follower_id
                            # print follower
                            followers.append(follower)
                        # print followers
                        return followers

                            # print follower_name, follower_id
                            # cnt3 += 1
                            # worksheet3.write(row3 + 1,col3, owner_username)
                            # worksheet3.write(row3 + 1,col3 + 1, owner_id)
                            # worksheet3.write(row3 + 1,col3 + 2, follower_name)
                            # worksheet3.write(row3 + 1,col3 + 3, follower_id)
                            # row3 += 1
                    try:
                        url2 = results2['pagination']['next_url']
                        # print url2
                        cnt4 += 1
                        # Setting the intervals between each calls
                        time.sleep(1)
                    except:
                        done2 = True

#helper functions
def call_api(url,params):
	data = urllib.urlencode(params)
	url = url + '?' + data
	req = urllib2.Request(url)
	result = json.loads(urllib2.urlopen(req).read())
	return result

def call_api1(url):
	req = urllib2.Request(url)
	result = json.loads(urllib2.urlopen(req).read())
	return result

if __name__ == '__main__':
    try:
        hashtag = sys.argv[1]
    except IndexError:
        print 'Usage: python cr_102.py <tag> <num of records>'

    if len(sys.argv) >= 3:
        num_photos = int(sys.argv[2])
        instaPost(hashtag, total=num_photos)
    else:
        instaPost(hashtag)

