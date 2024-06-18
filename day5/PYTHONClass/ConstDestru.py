# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 14:32:00 2024

@author: UD SYSTEMS
"""

#class with constructor and destructor

class Point:
   # parameterized constructor
   def __init__(self, x=0, y=0):
      self.x = x
      self.y = y

   def showXY(self):
      print("x = ", self.x)
      print("y=",self.y)
      
   # Destructor in python
   def __del__(self):
      class_name = self.__class__.__name__
      print (class_name, "destroyed")

pt1 = Point(1,2)
pt2 = Point(2,6)
pt3 = Point(5,9)

pt1.showXY()
pt2.showXY()
pt3.showXY()

print ("pt1 object id :",id(pt1))
print ("pt2 object id :",id(pt2))
print ("pt3 object id :",id(pt3)) # prints the ids of the obejcts

del pt1
del pt2
del pt3
