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


# in operator returns true when string contains the given characters
print('in Operator Output')
flag='v' in fullName
if flag:
    print("character found")
else:
    print("character not found")
    
# not in operator returns true when string don't contains the given characters
print('not in Operator Output')
flag='Z' not in fullName
if flag:
    print("character found")
else:
    print("character not found")      
    
# reverse a string
print('Reverse a given string')
print(fullName[::-1])
print(fullName[1:9:3]) #Start Index Pos: End Index Pos: Step
#012345678910111213141516
#Harshitha Jampala
