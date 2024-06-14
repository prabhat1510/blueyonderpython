# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 15:17:59 2024

@author: UD SYSTEMS
"""

def display(msg):
    print(msg)
    
    
#greetings is an higher order function which takes another another function as an argument
def greetings(message,disp):
    disp(message)#Calling the display function
    print("I am inside greeting")
    
    
greetings("Good Afternoon All !!!", display)# Calling the higher order function greetings

#()=>{}
dis = lambda m: print(m) #lambda function is a function without name
greetings("Hello All !!!",dis)


greetings("Hello Lambda !!!",lambda m: print(m))

dis("BlueYonder")