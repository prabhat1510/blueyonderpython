# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 13:02:07 2024

@author: UD SYSTEMS
"""

import userdefinedexample
from customernotfoundexception import CustomerNotFoundException
#Write a program to search a customer by customer ID 


#Exceptions handled using try and except       
try:
    custId =  int(input("Enter the customer id to be searched : "))
    userdefinedexample.findCustomerById(custId) #We know this method will throw or raise an exception 
except CustomerNotFoundException as c: #Here we are handling exception raised
     print(f'{c}')

print("After try and except block")
