# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 09:56:40 2024

@author: UD SYSTEMS
"""

import MySQLdb

hostname = 'localhost'
username = 'root'
password = 'password'
database = 'test_database'

# Collecting course details
courseid=int(input("Enter course id to be deleted :"))

try:
    # connecting to the mysql database
    conn= MySQLdb.connect( host=hostname, user=username, passwd=password, db=database )

    # opening the cursor
    cr = conn.cursor()

    strDelete="DELETE FROM course WHERE courseid=%s"

    #sending sql queries
    cr.execute(strDelete,([courseid]))
   
    # save data to database
    conn.commit()
    print("deleted")
except Exception:
    print("Exception Raised")
    if conn:
        conn.rollback()
finally:
    if conn:
        conn.close()
