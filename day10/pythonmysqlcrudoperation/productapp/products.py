# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 12:13:04 2024

@author: UD SYSTEMS
"""

import MySQLdb

hostname = 'localhost'
username = 'root'
password = 'password'
database = 'test_database'


def searchProductById(prodId):
    try:
        # Collecting course details
        
        # connecting to the mysql database
        conn= MySQLdb.connect( host=hostname, user=username, passwd=password, db=database )
    
        # opening the cursor
        cr = conn.cursor()
        
                  
        searchById="SELECT * FROM product_details where id=%s)"
    
        cr.execute(searchById,([prodId]))
        #printing all the records
        product = cr.fetchone()   
        
        # save data to database
        conn.commit()
                
        return product
   
    except Exception as e:
        print(e)
        print("Exception Raised ")
        if conn:
            conn.rollback()
    finally:
        if conn:
            conn.close()
    

def searchProductByName(prodName):
    try:
        # Collecting course details
        
        # connecting to the mysql database
        conn= MySQLdb.connect( host=hostname, user=username, passwd=password, db=database )
    
        # opening the cursor
        cr = conn.cursor()
        
                  
        searchById="SELECT * FROM product_details where name=%s)"
    
        cr.execute(searchById,([prodName]))
        #printing all the records
        product = cr.fetchOne()   
        
        # save data to database
        conn.commit()
                
        return product
   
    except Exception as e:
        print(e)
        print("Exception Raised ")
        if conn:
            conn.rollback()
    finally:
        if conn:
            conn.close()


