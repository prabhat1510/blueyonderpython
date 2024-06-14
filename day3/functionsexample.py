# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 09:47:20 2024

@author: UD SYSTEMS
"""

def calculate(num1,num2):
    sum=num1+num2
    return sum

print(calculate(15, 10))
print(calculate)   
print(type(calculate))   

print('*******************************************')
def add(a,b):
    return a+b # it will concatenate the two strings
    #return int(a)+int(b) #it will convert string into numbers and then addition

def get_input():
    in1= input("Enter first item or nothing to exit: ")
    return in1

while True:
    in1 =get_input()
    if in1=="":
        break
    in2 =get_input()
    if in2=="":
        break
    result =add(in1,in2)
    #print(f"{in1} + {in2} returns {result} \n")
    print(f"{in1} + {in2} returns {result} \n")