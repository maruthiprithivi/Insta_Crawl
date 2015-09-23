__author__ = 'data.team'

con = open('token1.txt','r')
tok = con.readlines()
n = 0
cnt = 20
done = False
# for i in tok:

while (done == False):
    if n <= 4:
        print "Printing token: %s" % (n+1)
        print tok[n]
        n += 1
        # cnt = cnt -1
    else:
        n = 0
    # cnt = cnt -1
    # if cnt == 0:
    #     done = True
print "Its sound"