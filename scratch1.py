def instaHandlePost(userId, total=100):
    # Getting the Handle Summary Info
    userInfo = instaUserInfo(userId)
    mediaCount = userInfo[0]
    followedByCount = userInfo[1]
    followingCount = userInfo[2]
    userName = userInfo[3]

    ## Playing the fool here --> Starting here!!
    cnt0 = 0
    row0 = 0
    col0 = 0
    row1 = 0
    col1 = 0
    row2 = 0
    col2 = 0
    row3 = 0
    col3 = 0
    row4 = 0
    col4 = 0
    flError = 0
    # row5 = 0
    # col5 = 0
    unique_followerId = []
    unique_userId = []
    unique_mediaId = []
    post_tag = list()
    counter = total
    done1 = False

    workbook = xlS.Workbook("output/" + userName + "_handle.xlsx")
    worksheet0 = workbook.add_worksheet('Summary')
    worksheet1 = workbook.add_worksheet('Posts')
    worksheet2 = workbook.add_worksheet('Tags')
    worksheet3 = workbook.add_worksheet('comments')
    worksheet4 = workbook.add_worksheet('Followers')
    worksheet99 = workbook.add_worksheet('Error Logs')
    # worksheet4 = workbook.add_worksheet('User Summary')
    # worksheet5 = workbook.add_worksheet('Likes Info')
    worksheet0.write(row0, col0, "owner_id")
    worksheet0.write(row0, col0 + 1, "owner_name")
    worksheet0.write(row0, col0 + 2, "media_count")
    worksheet0.write(row0, col0 + 3, "followed_by_count")
    worksheet0.write(row0, col0 + 4, "follow_count")

    worksheet1.write(row1, col1, "username")
    worksheet1.write(row1, col1 + 1, "user_handle")
    worksheet1.write(row1, col1 + 2, "caption")
    worksheet1.write(row1, col1 + 3, "post_link")
    worksheet1.write(row1, col1 + 4, "created_on")
    worksheet1.write(row1, col1 + 5, "media_id")
    worksheet1.write(row1, col1 + 6, "comment_count")
    worksheet1.write(row1, col1 + 7, "like_count")
    worksheet1.write(row1, col1 + 8, "post_type")
    worksheet2.write(row2, col2, "media_id")
    worksheet2.write(row2, col2 + 1, "tags")

    worksheet3.write(row3, col3, "comment")
    worksheet3.write(row3, col3 + 1, "comment_time")
    worksheet3.write(row3, col3 + 2, "commenter_name")
    worksheet3.write(row3, col3 + 3, "commenter_id")
    worksheet3.write(row3, col3 + 4, "media_id")

    worksheet4.write(row4, col4, "owner_id")
    worksheet4.write(row4, col4 + 1, "follower_id")
    worksheet4.write(row4, col4 + 2, "follower_name")
    worksheet4.write(row4, col4 + 3, "media_count")
    worksheet4.write(row4, col4 + 4, "followed_by_count")
    worksheet4.write(row4, col4 + 5, "follow_count")

    ## Playing the fool here --> Ending here!!
    worksheet0.write(row0 + 1, col0, userId)
    worksheet0.write(row0 + 1, col0 + 1, userName)
    worksheet0.write(row0 + 1, col0 + 2, mediaCount)
    worksheet0.write(row0 + 1, col0 + 3, followedByCount)
    worksheet0.write(row0 + 1, col0 + 4, followingCount)
    # Not necessary to have this, but just in case!
    row0 += 1


    url1 = 'https://api.instagram.com/v1/users/' + userId + '/media/recent/'
    # WunSG access token
    params1 = {'client_id' : '297d1f6458554ee8b87d0aff6e345d75'}

    cnt1 = 0
    cnt2 = 0
    while (done1 == False):

        # # Getting the Followers of the Handle
        # userFollowers = instaFollowers(userId)
        # for userFollower in userFollowers:
        #
        #     followerName = userFollower[0]
        #     followerI = userFollower[1]
        #     cnt0 += 1
        #     # print cnt0
        #     try:
        #         if followerI not in unique_followerId:
        #         # To get the unique user handles for crawling out followers
        #             unique_followerId.append(followerI)
        #             # To get the followers summary
        #             followerCount = instaUserInfo(followerI)
        #             mediaCount = followerCount[0]
        #             followedByCount = followerCount[1]
        #             followingCount = followerCount[2]
        #             worksheet4.write(row4 + 1, col4, userId)
        #             worksheet4.write(row4 + 1, col4 + 1, followerI)
        #             worksheet4.write(row4 + 1, col4 + 2, followerName)
        #             worksheet4.write(row4 + 1, col4 + 3, mediaCount)
        #             worksheet4.write(row4 + 1, col4 + 4, followedByCount)
        #             worksheet4.write(row4 + 1, col4 + 5, followingCount)
        #             row4 += 1
        #     except:
        #         flError += 1





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
            post_tags = item['tags']
            for tg in post_tags:
                tg = tg.encode('ascii','ignore')
                post_tag.append(tg)
            for tag in post_tag:
                worksheet2.write(row2 + 1, col2, media_id)
                worksheet2.write(row2 + 1, col2 + 1, tag)
                post_tag = []
                row2 += 1
            mediaComments = instaComment(media_id)
            try:
                for mediaCom in mediaComments:
                    # print mediaCom
                    # print len(mediaCom)
                    comment = mediaCom[3]
                    comment_time = mediaCom[0]
                    commenter_name = mediaCom[1]
                    commenter_id = mediaCom[2]
                    worksheet3.write(row3 + 1, col3, comment)
                    worksheet3.write(row3 + 1, col3 + 1, comment_time)
                    worksheet3.write(row3 + 1, col3 + 2, commenter_name)
                    worksheet3.write(row3 + 1, col3 + 3, commenter_id)
                    worksheet3.write(row3 + 1, col3 + 4, media_id)
                    row3 += 1
            except:
                comment = mediaComments[3]
                comment_time = mediaComments[0]
                commenter_name = mediaComments[1]
                commenter_id = mediaComments[2]
                worksheet3.write(row3, col3, comment)
                worksheet3.write(row3, col3 + 1, comment_time)
                worksheet3.write(row3, col3 + 2, commenter_name)
                worksheet3.write(row3, col3 + 3, commenter_id)
                worksheet3.write(row3, col3 + 4, media_id)
                row3 += 1



            worksheet1.write(row1 + 1,col1, owner_username)
            worksheet1.write(row1 + 1,col1 + 1, owner_id)
            worksheet1.write(row1 + 1,col1 + 2, post_caption)
            worksheet1.write(row1 + 1,col1 + 3, post_link)
            worksheet1.write(row1 + 1,col1 + 4, post_created)
            worksheet1.write(row1 + 1,col1 + 5, media_id)
            worksheet1.write(row1 + 1,col1 + 6, comment_count)
            worksheet1.write(row1 + 1,col1 + 7, like_count)
            worksheet1.write(row1 + 1,col1 + 8, post_type)
            row1 += 1
            # To print out the stalk log!! LOL!!
            cnt2 += 1




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
                    print "Total number of followers ", cnt0
    workbook.close()
