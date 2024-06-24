# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 15:14:59 2024

@author: UD SYSTEMS
"""
import MySQLdb

hostname = 'localhost'
username = 'root'
password = 'password'
database = 'test_database'


cname = input("Enter the name of the course to be searched ")

# connecting to the mysql database
conn= MySQLdb.connect( host=hostname, user=username, passwd=password, db=database )

# opening the cursor
cr = conn.cursor() 

# Query statement
#getAllCourse = "SELECT * FROM course"
courseByName = "SELECT * FROM course where  coursename = %s"

# Sending the query statement
#cr.execute(getAllCourse)
#Second argument is the parameter
cr.execute(courseByName,(cname,))

#printing all the records
courseTuple = cr.fetchall()
print(courseTuple)

#courseList = list()
#for row in cr.fetchall():
#    courseList.append(row)

print("**********************************************")
#print(courseList)


#closing the connection
conn.close()
