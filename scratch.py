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

    workbook = xlS.Workbook("output/" + tag + "_hashTag.xlsx")
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
    worksheet1.write(row1, col1 + 9, "owner_media_count")
    worksheet1.write(row1, col1 + 10, "follower_by_count")
    worksheet1.write(row1, col1 + 11, "following_count")
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
        if cnt1 < 1:
            startTime = timeit.default_timer()
            # print url1
            results1 = call_api(url1, params1)
            data1 = results1['data']
        else:
            results1 = call_api1(url1)
            data1 = results1['data']

        for item in data1:
        # To parse the data set into separate segments
            owner_username = item['user']['username']
            owner_id = item['user']['id']
            # Getting user info
            owner_info = instaUserInfo(owner_id)
            owner_media_count = owner_info[0]
            owner_follower_count = owner_info[1]
            owner_follows_count = owner_info[2]
            post_tags = item['tags']
            for tg in post_tags:
                tg = tg.encode('ascii','ignore')
                post_tag.append(tg)
            try:
                post_caption = item['caption']['text']
                post_caption = post_caption.encode('ascii','ignore')
            except:
                post_caption = " "
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
            for tag in post_tag:
                worksheet2.write(row2 + 1, col2, media_id)
                worksheet2.write(row2 + 1, col2 + 1, tag)
                post_tag = []
                row2 += 1
            # row = 0
            worksheet1.write(row1 + 1,col1, owner_username)
            worksheet1.write(row1 + 1,col1 + 1, owner_id)
            worksheet1.write(row1 + 1,col1 + 2, post_caption)
            worksheet1.write(row1 + 1,col1 + 3, post_link)
            worksheet1.write(row1 + 1,col1 + 4, post_created)
            worksheet1.write(row1 + 1,col1 + 5, media_id)
            worksheet1.write(row1 + 1,col1 + 6, image_url)
            worksheet1.write(row1 + 1,col1 + 7, comment_counts)
            worksheet1.write(row1 + 1,col1 + 8, likes_counts)
            worksheet1.write(row1 + 1,col1 + 9, owner_media_count)
            worksheet1.write(row1 + 1,col1 + 10, owner_follower_count)
            worksheet1.write(row1 + 1,col1 + 11, owner_follows_count)
            row1 += 1
            cnt2 += 1
            print cnt2, " posts crawled!!!"

            # # Followers call kicks in!!
            # if owner_id not in unique_userId:
            #     # print owner_id
            #     # To get the unique user handles for crawling out followers
            #     unique_userId.append(owner_id)
            #
            #     followers = instaFollowers(owner_id)
            #     # print followers
            #     for follower in followers:
            #         # print follower
            #         follower_name = follower[0]
            #         follower_id = follower[0]
            #         worksheet3.write(row3 + 1,col3, owner_username)
            #         worksheet3.write(row3 + 1,col3 + 1, owner_id)
            #         worksheet3.write(row3 + 1,col3 + 2, follower_name)
            #         worksheet3.write(row3 + 1,col3 + 3, follower_id)
            #         row3 += 1
        """
        else:
            results1 = call_api1(url1)
            data1 = results1['data']
            for item in data1:
            # To parse the data set into separate segments
                owner_username = item['user']['username']
                owner_id = item['user']['id']
                # Getting user info
                owner_info = instaUserInfo(owner_id)
                owner_media_count = owner_info[0]
                owner_follower_count = owner_info[1]
                owner_follows_count = owner_info[2]

                post_tags = item['tags']
                for tg in post_tags:
                    tg = tg.encode('ascii','ignore')
                    post_tag.append(tg)
                try:
                    post_caption = item['caption']['text']
                    post_caption = post_caption.encode('ascii','ignore')
                except:
                    post_caption = " "
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
                for tag in post_tag:
                    worksheet2.write(row2 + 1, col2, media_id)
                    worksheet2.write(row2 + 1, col2 + 1, tag)
                    row2 += 1
                # row = 0
                worksheet1.write(row1 + 1,col1, owner_username)
                worksheet1.write(row1 + 1,col1 + 1, owner_id)
                worksheet1.write(row1 + 1,col1 + 2, post_caption)
                worksheet1.write(row1 + 1,col1 + 3, post_link)
                worksheet1.write(row1 + 1,col1 + 4, post_created)
                worksheet1.write(row1 + 1,col1 + 5, media_id)
                worksheet1.write(row1 + 1,col1 + 6, image_url)
                worksheet1.write(row1 + 1,col1 + 7, comment_counts)
                worksheet1.write(row1 + 1,col1 + 8, likes_counts)
                worksheet1.write(row1 + 1,col1 + 9, owner_media_count)
                worksheet1.write(row1 + 1,col1 + 10, owner_follower_count)
                worksheet1.write(row1 + 1,col1 + 11, owner_follows_count)
                row1 += 1
                cnt2 += 1
                print cnt2, " posts crawled!!!"


                # Followers call kicks in!!
                if owner_id not in unique_userId:
                    # print owner_id
                    # To get the unique user handles for crawling out followers
                    unique_userId.append(owner_id)

                    followers = instaFollowers(owner_id)
                    # print followers
                    for follower in followers:
                        # print follower
                        follower_name = follower[0]
                        follower_id = follower[1]
                        worksheet3.write(row3 + 1,col3, owner_username)
                        worksheet3.write(row3 + 1,col3 + 1, owner_id)
                        worksheet3.write(row3 + 1,col3 + 2, follower_name)
                        worksheet3.write(row3 + 1,col3 + 3, follower_id)
                        row3 += 1
            """
                # print out_data
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
    workbook.close()
