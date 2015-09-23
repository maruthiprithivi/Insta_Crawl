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
            else:
                print "Goodaaaaa!!!"

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



users = {1176696,
1960324402,
12874594  ,
38544513  ,
520467180 ,
334239435 ,
7270872   ,
1093323199,
176028489 ,
175485485 ,
48350736  ,
3209641   ,
46474876  ,
6613612   ,
262378316 ,
1856150   ,
1038271   ,
185960284 ,
531180927 ,
10330644  ,
1667864472,
8799455   ,
1659190   ,
3635899   ,
2213346   ,
3874447   ,
1194980   ,
13314363  ,
38033409  ,
55994584  ,
51417049  ,
1342683   ,
1925445115,
206289604 ,
206289604 ,
2598794   ,
39057665  ,
1114893   ,
3251156   ,
31437225  ,
1193195876,
39211673  ,
1028191623,
42397549  ,
15374013  ,
2081573   ,
200352262 ,
1992921   ,
42850644  ,
2542123   ,
697476    ,
18854090  ,
844869    ,
5120798   ,
216381817 ,
792372    ,
46017093  ,
411976174 ,
12026951  ,
50175707  ,
1812650   ,
41918387  ,
31173628  ,
611902940 ,
50370271  ,
50370271  ,
10337764  ,
5664415   ,
794087    ,
30581341  ,
13985357  ,
13985357  ,
41172497  ,
4791505   ,
173654913 ,
16270169  ,
182031511 ,
15682883  ,
33052616  ,
1230427684,
1550024977,
8540298   ,
514669595 ,
45238692  ,
20646576  ,
19612250  ,
203677556 ,
15510161  ,
3032199  ,
23241728  ,
20535040  ,
222151663 ,
20012750  ,
192974291 ,
7057308   ,
180874825 ,
104864424 ,
18193927  ,
272839347 ,
74741    ,
372876100 ,
230518279 ,
3005822   ,
10909047  ,
6016577   ,
19494     ,
7988719   ,
43508592  ,
12690060  ,
1940166266,
1217108   ,
29944867  ,
15413965  ,
104812330 ,
50669372  ,
29228317  ,
3336545   ,
178004518 ,
12695412  ,
6272933   ,
870048    ,
345586825 ,
1264168275,
24913760  ,
31906348  ,
15168480  ,
10708984  ,
2033552   ,
4479106   ,
250385892 ,
52890422  ,
4538924   ,
228682459 ,
55659861  ,
5091021   ,
468298337 ,
146185492 ,
14542353  ,
232162042 ,
33943961  ,
38098008  ,
16081385  ,
22821371  ,
184056803 ,
303044499 ,
2398543  ,
1795643958,
384404983 ,
29245443  ,
13110841  ,
31187389  ,
23596482  ,
209770391 ,
52081855 ,
1037057512,
1154925   ,
50221730  ,
1137477   ,
245709729 ,
13330101  ,
282435586 ,
653086494 ,
24702811  ,
1197554857,
8613432   ,
1019944   ,
293747438 ,
32320084  ,
1474770139,
29724682  ,
23775549  ,
664866492 ,
1513734   ,
244114601 ,
1554469   ,
295966821 ,
24787282  ,
837697229 ,
33117302  ,
2783791   ,
804332    ,
1269043127,
2284100   ,
1007234   ,
305179017 ,
3990785   ,
296262118 ,
273567213 ,
1073981   ,
7739517   ,
227363336 ,
174317071 ,
1495567344,
186503859 ,
2285842   ,
509886076 ,
2282149   ,
176060865 ,
1960324402,
146068081 ,
2972235   ,
1547406563,
266430793 ,
9446281   ,
501083379 ,
13701679  ,
608276910 ,
3304075   ,
34363497  ,
36967270  ,
18198910  ,
179377470 ,
24723375  ,
1214954779,
11624106  ,
1510899667,
12591395  ,
51927870  ,
21359700  ,
1598540   ,
368423779 ,
1328394   ,
1553617684,
259176609 ,
48702383  ,
1356810113,
177646247 ,
3951198   ,
35927749  ,
2253384   ,
2708925   ,
31906348  ,
8341871  ,
2178693163,
2430332   ,
7534433   ,
190458270 ,
5929125   ,
1239191   ,
2017798600,
344662085 ,
15893822  ,
181706098 ,
336267819 ,
20850451  ,
360192690 ,
1016481194,
268981238 ,
233524858 ,
1108581211,
458090115 ,
4850164   ,
1805634   ,
924653    ,
530867511 ,
1447070412,
2014987   ,
12294825  ,
217760689 ,
2676692   ,
4967559   ,
54373688  ,
1419392595,
2707406   ,
1790347   ,
1416615337,
33962775  ,
44648694  ,
2017675303,
49325559  ,
231237338 ,
1444451   ,
4293670   ,
14127724  ,
16332875  ,
54327853  ,
358053405 ,
45375745  ,
245108113 ,
540201740 ,
443097382 ,
443097382 ,
550302977 ,
1313459064,
30701867  ,
31346017  ,
53304359  ,
181381221 ,
54223451  ,
173682889 ,
203234226 ,
204451992 ,
270834955 ,
273913286 ,
1614552431,
34038137  ,
2414270   ,
50356634  ,
8794221   ,
243344971 ,
8689755   ,
286096258 ,
25146165  ,
537628974 ,
379767707 ,
178457492 ,
8858492   ,
26316882  ,
251727766 ,
13029987  ,
529433531 ,
23384364  ,
144950966 ,
1383616137,
24710005  ,
22287528  ,
13680798  ,
247251702 ,
145276241 ,
14063433  ,
1533082687,
1918541966,
1918541966,
35926143  ,
8858492   ,
2512588   ,
51235038  ,
2068573   ,
197553049 ,
12912100  ,
189969859 ,
14469844  ,
373406471 ,
1719643   ,
272342131 ,
26913335  ,
185854451 ,
22935269  ,
266084535 ,
372958001 ,
918802971 ,
75940    ,
9325266   ,
185115449 ,
329421004 ,
54713775  ,
185953913 ,
13566197 }

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
workbook = xlS.Workbook("output/safraInfluencers.xlsx")
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

workbook.close()

print "Taaa Daaaa!!! TGIF!!! Go Home Sleeppppppp!"

