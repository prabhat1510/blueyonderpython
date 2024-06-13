# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 09:56:57 2024

@author: UD SYSTEMS
"""

# String operators

firstName=input("Enter First Name : ")
lastName=input("Enter the Last Name : ")

# + concatenation
fullName=firstName+" "+lastName
print('Operator + Output')
print("Full Name : ", fullName)

# : Range or slicing
print('Operator : Output')
print("Slice :", fullName[2:6])

# * repeation
print('Operator * Output')
print("slicing :", (fullName+" ")*3)

# r/R - rawstring  removes the meaning for the special character
print('Operator r/R Output')
print("Full Name is :\n", fullName)
print(r"Full Name is : \n", fullName)
print(R"Full Name is : \n", fullName)