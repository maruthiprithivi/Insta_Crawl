__author__ = 'Maruthi'

import urllib,urllib2,os,sys
import json,time
import csv,re
import xlsxwriter as xlS


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
            user_bio = results3['data']['bio']
            if len(user_bio) < 1:
                user_bio = "No Bio Lahhhhhhhhh!!!"
            # else:
                # print "Goodaaaaa!!!"

            useR = media_count, follower_count, follow_count, user_name, user_bio
            # userCount.append(useR)
            return useR

        except:
            media_count = "Private Profile"
            follower_count = "Private Profile"
            follow_count = "Private Profile"
            user_name = "Private Profile"
            user_bio = "Private Profile"
            useR = media_count, follower_count, follow_count, user_name, user_bio
            return useR

#helper functions
def call_api(url,params):
    try:
        data = urllib.urlencode(params)
        url = url + '?' + data
        # print url
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



users = {
    1392487,
13113023,
8247979,
3620456,
174924244,
2144627,
24623409,
13410204,
194850629,
13651373,
2204247,
18991728,
269993546,
8531540,
1358641689,
1462212983,
217653153,
1266894032,
146164422,
235242176,
370180681,
245077265,
5714015,
351442652,
2752620,
218294544,
442616921,
259720217,
53561576,
540392497,
14032309,
195533409,
300591799,
440313239,
10528007,
287798895,
296262118,
7650331,
27932763,
200637946,
3544369,
210640207,
283559004,
14063433,
1181152569,
4978212,
1080975417,
201032226,
452019406,
259155555,
376966113,
15950551,
8940640,
8613445,
1634978262,
947843,
421547362,
1624157587,
53038597,
10295295,
507279041,
781876,
704524154,
216757910,
1587600386,
4999849,
1539058457,
1722659,
53253159,
1482758646,
868058015,
211428595,
1090055,
21205777,
111655,
30621191,
573694513,
1538137944,
145710391,
28700918,
1879151,
33277136,
27804109,
17156893,
479647,
1953653,
217234390,
462454743,
506364508,
470087978,
1600888876,
34797366,
129108,
10337764,
27622521,
5120798,
50702117,
19448743,
333558028,
39311966,
1326725,
33907093,
4554155,
381714914,
1392390920,
4433620,
439880468,
6260449,
49641867,
1223151170,
319494887,
3433981,
1138605,
216250717,
1351522,
6228629,
2032666108,
54815032,
195229878,
30686462,
26530164,
342389134,
365352906,
3767367,
215368881,
29331857,
208934167,
1594908,
4826548,
437416792,
12954559,
5521683,
353704480,
1113921,
255972439,
665020261,
186734703,
1017990,
511346564,
671152448,
1406950115,
903338344,
336320468,
227487635,
11742440,
264217957,
256983420,
1033027,
190637257,
972311,
331993056,
335324928,
986281113,
2641062,
10531660,
342204225,
219777478,
567469627,
22207198,
18428278,
223218227,
20814201,
7348713,
1545733529,
4432329,
495121998,
1680184934,
1876622,
402938204,
2327418,
284747639,
386673780,
1739210645,
26962743,
241973343,
191651975,
20957044,
586311669,
363666667,
231949310,
884733672,
1700586551,
4268403,
842474,
191687597,
589247082,
17881031,
1580163759,
504325373,
144071141,
2132940349,
1147036351,
1517236244,
1071288682,
1074702317,
9330176,
9301559,
411553635,
1720060574,
3117840,
200515970,
2128930429,
10481782,
1481948184,
387307203,
38320701,
511530036,
195121475,
205880301,
894128104,
33085039,
1970955610,
1439508928,
963028145
}

# if __name__ == '__main__':
#     try:
#         userHandle = sys.argv[1]
#     except IndexError:
#         print 'Usage: python userInfoLoop.py start"
#
#     if len(sys.argv) >= 3:
#         posts = int(sys.argv[2])
#         instaUserInfo(userHandle,)
#         # print "posts: ", posts
#         for user in users:
#
#
#     else:
#         instaFollowers(userHandle)
row0 = 0
col0 = 0
workbook = xlS.Workbook("output/stbInfluencers.xlsx")
worksheet0 = workbook.add_worksheet('InfluencersInfo')
worksheet0.write(row0, col0, "owner_id")
worksheet0.write(row0, col0 + 1, "owner_name")
worksheet0.write(row0, col0 + 2, "media_count")
worksheet0.write(row0, col0 + 3, "no_of_followers")
worksheet0.write(row0, col0 + 4, "Bio")

for user in users:

    # try:
    userData = instaUserInfo(str(user))
    worksheet0.write(row0 + 1, col0, user)
    worksheet0.write(row0 + 1, col0 + 1, userData[3])
    worksheet0.write(row0 + 1, col0 + 2, userData[0])
    worksheet0.write(row0 + 1, col0 + 3, userData[1])
    worksheet0.write(row0 + 1, col0 + 4, userData[4])
    row0 += 1
    print "HAKUNA mAtAtA!!! x%s " % row0

workbook.close()

print "HAKUNA mAtAtAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa!!!"

