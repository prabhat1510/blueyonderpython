# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 16:27:48 2024

@author: UD SYSTEMS
"""

# string problem

nm=input("Enter Your Name :")

nm1=nm[0:2] #slicing
nm2=nm[-2:len(nm)] #slicing
print(nm1)
print(nm2)

n1=nm1
n2=nm2

nm3=nm.replace(nm1,"")
nm4=nm3.replace(nm2,"")
print(nm3)
print(nm4)
nm5=nm2+nm4+nm1
print(nm5)