__author__ = 'data.team'

import re

# con = open('token1_1.txt','r')
#
# for i in con:
#     # print len(i)
#     x = i.split(",")
#     print len(x)

# print len(con)


f = "https://api.instagram.com/v1/users/387804605/media/recent?max_id=1072739449353796117_387804605&client_id=5b77a83635ce4fcbbce5293f2e5314d4"

f1 = f.find("&")
print f[:f1+11]