# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 14:15:44 2024

@author: UD SYSTEMS
"""
#Defined a Dog class with propeties
class Dog:
    #properties or attribute or data fields
    breed='Pug'
    color=''
    size=''
    weight=''
    
    #methods 
    def eat(__self__):
        print('Eating')
    
    def sleep(__self__):
        print('Sleeping')
        

#Object dog1 is created by calling Dog() default constructor
dog1 = Dog()
print(dog1.eat())
print(dog1.sleep())
print(dog1.breed)