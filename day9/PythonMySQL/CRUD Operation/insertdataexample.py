# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 15:03:32 2024

@author: UD SYSTEMS
"""

import MySQLdb

hostname = 'localhost'
username = 'root'
password = 'password'
database = 'test_database'


# Collecting course details
courseid=int(input("Enter course id :"))
cname=input("Enter Course Name :")
fees=int(input("Enter fees amount :"))


try:
    # connecting to the mysql database
    conn= MySQLdb.connect( host=hostname, user=username, passwd=password, db=database )

    # opening the cursor
    cr = conn.cursor()

    strInsert="INSERT INTO course(courseid,coursename,fees) VALUES(%s,%s,%s)"


    #sending sql queries
    cr.execute(strInsert,([courseid,cname,fees]))
       

    # save data to database
    conn.commit()
    print("Records added")
except Exception as e:
    print(e)
    print("Exception Raised ")
    if conn:
        conn.rollback()
finally:
    if conn:
        conn.close()