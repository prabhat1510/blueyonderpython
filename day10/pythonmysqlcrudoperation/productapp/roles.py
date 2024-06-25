# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 10:52:41 2024

@author: UD SYSTEMS
"""

'''
    CRUD operation of roles
'''
import MySQLdb
from RoleNotFoundException import RoleNotFoundException 
hostname = 'localhost'
username = 'root'
password = 'password'
database = 'test_database'



def  createRoles(rolename):
    try:
        # connecting to the mysql database
        conn= MySQLdb.connect( host=hostname, user=username, passwd=password, db=database )
    
        # opening the cursor
        cr = conn.cursor()
        
                  
        strInsert="INSERT INTO roles(rolename) VALUES(%s)"
    
        cr.execute(strInsert,([rolename]))
            
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

def  findRoleById(roleid):
    try:
        
        # connecting to the mysql database
        conn= MySQLdb.connect( host=hostname, user=username, passwd=password, db=database )
    
        # opening the cursor
        cr = conn.cursor()
        
                  
        findRoleById="SELECT * FROM roles where roleid=%s"
    
        cr.execute(findRoleById,([roleid]))
           
        role = cr.fetchone()
        
        # save data to database
        conn.commit()
        if(role == None):
            raise RoleNotFoundException("Role with id "+str(roleid)+ " not found in record")
        else:
            return role
    except RoleNotFoundException as r:
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

def  findRoleByName(rolename):
    try:
        
        # connecting to the mysql database
        conn= MySQLdb.connect( host=hostname, user=username, passwd=password, db=database )
    
        # opening the cursor
        cr = conn.cursor()
        
                  
        findRoleByName="SELECT * FROM roles where rolename=%s"
    
        cr.execute(findRoleByName,([rolename]))
           
        role = cr.fetchone()
        # save data to database
        conn.commit()
        if(role == None):
            raise RoleNotFoundException("Role with name "+str(rolename)+ " not found in record")
        else:
            return role
    except RoleNotFoundException as r:
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


def  findRoles():
    try:
        
        # connecting to the mysql database
        conn= MySQLdb.connect( host=hostname, user=username, passwd=password, db=database )
    
        # opening the cursor
        cr = conn.cursor()
        
                  
        findRoles="SELECT * FROM roles"
    
        cr.execute(findRoles)
           
        roles = cr.fetchall()
        # save data to database
        conn.commit()
        if(roles == None):
            raise RoleNotFoundException("Roles not found in record")
        else:
            return roles
    except RoleNotFoundException as r:
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

#Code which calls createRoles has to pass rolename
# Collecting course details
#rolename=input("Enter role name :")
#createRoles(rolename)

#r= findRoleById(2)
#print(r)
r= findRoleByName('USERRRRR')
print(r)

print(findRoles())