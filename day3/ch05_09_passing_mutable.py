# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 12:19:04 2024

@author: UD SYSTEMS
"""

def add_10(add_10):
    for i in range(len(add_10)):
        add_10[i] += 10
    print("Inside add_10")
    print(" Local object = ",add_10)
    
mutable=[1,2,3]
#mutable=(1,2,3)
print("Outside add_10 before call")
print("     mutable object value= ", mutable)
#add_10(mutable)#Here we are passing reference
#add_10(mutable[:]) #passing values
add_10(list(mutable))#passing values
print("Outside add_10 after call")
print("     mutable object value= ", mutable)
print(list(mutable))
print(mutable)
