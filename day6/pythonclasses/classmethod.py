# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 12:08:51 2024

@author: UD SYSTEMS
"""

# class Method





#class declaration
class Demo1:
       # class variable declaration
    num=0
    def __init__(self, num1):
       #Demo1.num=num1 #Error
       self.num1=num1
    
       
    @classmethod 
    def showNum(self):
           #print("num : ", Demo1.num1) #Error
           #print("num1 : ", self.num1) #Error 
           print("num : ", self.num)

#object creation
obj1=Demo1(100)
obj2=Demo1(250)

obj1.showNum()
obj2.showNum()
#calling the classmethod with class name
Demo1.showNum()
Demo1.showNum()



