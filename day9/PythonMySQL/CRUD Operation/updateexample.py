# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 16:54:43 2024

@author: UD SYSTEMS
"""

import MySQLdb

hostname = 'localhost'
username = 'root'
password = 'password'
database = 'test_database'

cid = input("Enter the course id  ")
newcname = input("Enter the new name of the course to be updated ")

# connecting to the mysql database
conn= MySQLdb.connect( host=hostname, user=username, passwd=password, db=database )

# opening the cursor
cr = conn.cursor() 
 
#Query
updateQuery = "UPDATE course SET coursename=%s WHERE courseid=%s"
cr.execute(updateQuery,(newcname,cid))
# save data to database
conn.commit()

#closing the connection
conn.close()

