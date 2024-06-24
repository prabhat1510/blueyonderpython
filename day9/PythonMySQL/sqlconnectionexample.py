# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 14:04:14 2024

@author: UD SYSTEMS
"""


#from __future__ import print_function

hostname = 'localhost'
username = 'root'
password = 'password'
database = 'test_database'

# Simple routine to run a query on a database and print the results:
def doQuery( conn ) :
    cur = conn.cursor()

    cur.execute( "SELECT fname, lname FROM employee" )

    for firstname, lastname in cur.fetchall() :
        print( firstname, lastname )



def doInsert(conn):
    cur=conn.cursor()
    cur.execute("Insert into employee values(1,'Bill','Clinton')")

print( "Using mysqlclient (MySQLdb):" )
import MySQLdb
myConnection = MySQLdb.connect( host=hostname, user=username, passwd=password, db=database )
doInsert(myConnection)
doQuery( myConnection )
myConnection.close()

print( "Using mysql.connector:" )
import mysql.connector
myConnection = mysql.connector.connect( host=hostname, user=username, passwd=password, db=database )
doQuery( myConnection )
myConnection.close()

print( "Using pymysql:" )
import pymysql
myConnection = pymysql.connect( host=hostname, user=username, passwd=password, db=database )
doQuery( myConnection )
myConnection.close()