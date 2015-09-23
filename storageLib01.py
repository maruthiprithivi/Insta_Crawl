__author__ = 'Maruthi'

import psycopg2
import sys
import xlsxwriter as xlS

# handlePost = owner_id, owner_username, post_caption, post_created, comment_count, post_link, like_count, post_type, media_id, post_tag, media_link
# useR = media_count, follower_count, follow_count, user_name
# def userSummary(userInfoData, userName="Instagram"):
#     row2 = 0
#     col2 = 0
#     workbook = xlS.Workbook("output/" + userName + "_handle.xlsx")

def handleWriter(handlePostData, userName="Instagram"):
    row0 = 0
    row1 = 0
    col0 = 0
    col1 = 0
    workbook = xlS.Workbook("output/" + userName + "_handle.xlsx")
    worksheet0 = workbook.add_worksheet('Posts')
    worksheet1 = workbook.add_worksheet('tags')
    # Sheet 1 - Create
    worksheet0.write(row0, col0, "username")
    worksheet0.write(row0, col0 + 1, "user_handle")
    worksheet0.write(row0, col0 + 2, "caption")
    worksheet0.write(row0, col0 + 3, "post_link")
    worksheet0.write(row0, col0 + 4, "created_on")
    worksheet0.write(row0, col0 + 5, "media_id")
    worksheet0.write(row0, col0 + 6, "comment_count")
    worksheet0.write(row0, col0 + 7, "like_count")
    worksheet0.write(row0, col0 + 8, "post_type")
    worksheet0.write(row0, col0 + 9, "media_link")
    # Sheet 2 - Create
    worksheet1.write(row1, col1, "media_id")
    worksheet1.write(row1, col1 + 1, "tags")
    for oneRow in handlePostData:
        # Sheet 1 - Write
        worksheet0.write(row0 + 1,col0, oneRow[1])
        worksheet0.write(row0 + 1,col0 + 1, oneRow[0])
        worksheet0.write(row0 + 1,col0 + 2, oneRow[2])
        worksheet0.write(row0 + 1,col0 + 3, oneRow[5])
        worksheet0.write(row0 + 1,col0 + 4, oneRow[3])
        worksheet0.write(row0 + 1,col0 + 5, oneRow[8])
        worksheet0.write(row0 + 1,col0 + 6, oneRow[4])
        worksheet0.write(row0 + 1,col0 + 7, oneRow[6])
        worksheet0.write(row0 + 1,col0 + 8, oneRow[7])
        worksheet0.write(row0 + 1,col0 + 9, oneRow[10])
        row0 += 1
        # Sheet 2 - Write
        for tag in oneRow[9]:
            worksheet1.write(row1 + 1, col1, oneRow[8])
            worksheet1.write(row1 + 1, col1 + 1, tag)
            row1 += 1
    workbook.close()