# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 15:11:20 2024

@author: UD SYSTEMS
"""

import MySQLdb
 
hostname = 'localhost'
username = 'root'
password = 'password'
database = 'test_database'


def registerUser():
    print("To register you on our system we need few details :")
    fname=input("Enter your first name :")
    lname=input("Enter your last name :")
    mobile=input("Enter your mobile :")
    email=input("Enter your email :")
    address=input("Enter your address :")
    uname=input("Enter your username :")
    pword=input("Enter your password :")
    try:
        # connecting to the mysql database
        conn= MySQLdb.connect( host=hostname, user=username, passwd=password, db=database )
    
        # opening the cursor
        cr = conn.cursor()
        
                  
        strInsert="INSERT INTO user_details(fname,lname,mobile,email,address) VALUES (%s,%s,%s,%s,%s);"
        cr.execute(strInsert,([fname,lname,mobile,email,address]))
        userid = cr.lastrowid #Get the inserted userid value
        strUserInsert="INSERT INTO users(username,password,roleid,userid) VALUES(%s,%s,%s,%s)"
        cr.execute(strUserInsert,[uname,pword,1,userid])
            
        # save data to database
        conn.commit()
        print("User Registered Successfully")
    except Exception as e:
        print(e)
        print("Exception Raised ")
        if conn:
            conn.rollback()
    finally:
        if conn:
            conn.close()
    
    
registerUser()