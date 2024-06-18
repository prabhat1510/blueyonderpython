# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 14:24:22 2024

@author: UD SYSTEMS
"""

# Python class with constructor



#class declaration
class Car:
   
    # default Constructor
    def __init__(self,brand):
        self.__model_="Maruthi"   #private variable
        self.__color_="Green"
        self.__brand_=brand
    
    def showCarInfo(self):
        print("Car Model : ", self.__model_)
        print("Car Color : ", self.__color_)
        print("Car Brand : ", self.__brand_)

print("Example class with Default construtor example ")
#object creation
objC=Car("Suzuki") # calling default constructor

#calling the method using object
objC.showCarInfo()
#objC.__model_
#self.__model_

