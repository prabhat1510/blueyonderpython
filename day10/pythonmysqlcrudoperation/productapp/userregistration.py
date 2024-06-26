# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 15:11:20 2024

@author: UD SYSTEMS
"""

import MySQLdb
import sys
from UserNotFoundException import UserNotFoundException
from PasswordMismatchException import PasswordMismatchException
import products

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
    

    

def  findUserByName(uname):
    try:
        
        # connecting to the mysql database
        conn= MySQLdb.connect( host=hostname, user=username, passwd=password, db=database )
    
        # opening the cursor
        cr = conn.cursor()
        
                  
        findUserByName="SELECT * FROM users where username=%s"
    
        cr.execute(findUserByName,([uname]))
           
        user = cr.fetchone()
        
        if(user == None):
            raise UserNotFoundException("User with name "+str(uname)+ " not found in record")
        else:
            return user
    except UserNotFoundException as r:
        print(r)
        if conn:
            conn.rollback()
    except Exception as e:
        print(e)
        print("Exception Raised ")
        if conn:
            conn.rollback()
    finally:
        if conn:
            conn.close()    

def productWelcome(user):
     print("***************Welcome to Product Search******************")
     print("***************Select from below options***************")
     print("***************1. Create Product ********")
     print("***************2. Find Product by id *********************")
     print("***************3. Find Product by name *********************")
     print("***************4. Get all products *********************")
     print("***************5. To Exit enter 5**********************")
     while(True):
         
         choice = input("Enter appropriate option ")
         if(choice != "" and choice in ('1','2','3','4','5')):
             ch=int(choice)
             if(ch == 1):
                 if(user[3] == 2):
                     productname=input("Enter product name :")
                     price=int(input("Enter price product :"))
                     description=input("Enter product description :")
                     products.createProducts(productname, price, description)
                 else:
                     print("You don't have authority to add product")
                     break
                 #pass
             elif(ch == 2):
                 productId = input("Enter product id to be searched : ")
                 product = products.findProductById(productId)
                 print(product)
                 #return product
                 #pass
             elif(ch == 3):
                 productName=input("Enter product name for search : ")
                 product = products.findProductByName(productName)
                 print(product)
                 #return product
             elif(ch == 4):
                 prods = products.findProducts()
                 print(prods)
                 #return prods
             else:
                 break
                 #sys.exit(0)
         else:
             print("Enter correct options")

def login():
    try:
        uname=input("Enter username ")
        pword=input("Enter password ")
        user = findUserByName(uname)
        if(user != None):
            if(user[1] == uname): 
               if(user[2]==pword):
                print("user logged in successfully with role "+str(user[3]))
                #Product functionality
                productWelcome(user)
               else:
                   raise PasswordMismatchException("Password is not correct")
        else:
            raise UserNotFoundException("User with username "+uname+" doesn't exists")
    except PasswordMismatchException as p:
        print(p)
    except UserNotFoundException as u:
        print(u)
#registerUser()
#print(findUserByName("bill"))
#login("bill1","passwrd")
