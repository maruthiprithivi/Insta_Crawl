__author__ = 'maruthi'

import psycopg2
import sys
import xlsxwriter

# con = None

# try:
#
#     con = psycopg2.connect(database='postgres', user='postgres', password='P@ssw0rdDT')
#     cur = con.cursor()
#     cur.execute('SELECT version()')
#     ver = cur.fetchone()
#     print ver
#
#
# except psycopg2.DatabaseError, e:
#     print 'Error %s' % e
#     sys.exit(1)


cars1 = (
    (1, 'Audi', 52642),
    (2, 'Mercedes', 57127),
    (3, 'Skoda', 9000),
    (4, 'Volvo', 29000),
    (5, 'Bentley', 350000),
    (6, 'Citroen', 21000),
    (7, 'Hummer', 41400),
    (8, 'Volkswagen', 21600)
)

cars2 = (
    (11, 'Audi', 52642),
    (12, 'Mercedes', 57127),
    (13, 'Skoda', 9000),
    (14, 'Volvo', 29000),
    (15, 'Bentley', 350000),
    (16, 'Citroen', 21000),
    (17, 'Hummer', 41400),
    (18, 'Volkswagen', 21600)
)

con = None

try:
    try:
        print "cars1 run"
        # Connection Credentials
        con = psycopg2.connect(host='54.255.196.231', port='5432', database='postgres', user='postgres', password='P@ssw0rdDT')
        cur = con.cursor()
        # Creating a table
        cur.execute("CREATE TABLE Cars1(Id INT, Name TEXT, Price INT)")
        query = "INSERT INTO Cars1 (Id, Name, Price) VALUES (%s, %s, %s)"
        # Data source pointer
        cur.executemany(query, cars1)
        con.commit()

        # cur.execute("DROP TABLE IF EXISTS Cars")

    except:
        # Connection Credentials
        con = psycopg2.connect(host='54.255.196.231', port='5432', database='postgres', user='postgres', password='P@ssw0rdDT')
        cur = con.cursor()
        print "Second Logic in Progress"
        query = "INSERT INTO Cars1 (Id, Name, Price) VALUES (%s, %s, %s)"
        # Data source pointer
        cur.executemany(query, cars2)
        print "This Works!!"
        con.commit()

except psycopg2.DatabaseError, e:
    print 'Error %s' % e
    sys.exit(1)

# except psycopg2.DatabaseError, e:
#     if con:
#         con.rollback()
#
#     print 'Error %s' % e
#     sys.exit(1)

# try:
#     cur.execute("CREATE TABLE Cars2(Id INT PRIMARY KEY, Name TEXT, Price INT)")
#     query = "INSERT INTO Cars1 (Id, Name, Price) VALUES (%s, %s, %s)"
#     cur.executemany(query, cars1)
#     con.commit()
# except:
#     print "Second Logic in Progress"
#     query = "INSERT INTO Cars2 (Id, Name, Price) VALUES (%s, %s, %s)"
#     cur.executemany(query, cars2)
#     print "This Works!!"
#     con.commit()

finally:

    if con:
        con.close()