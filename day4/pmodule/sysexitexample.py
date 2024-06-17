# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 11:39:49 2024

@author: UD SYSTEMS
"""

# Example - sys module in python
import sys



while (True):
         y=int(input("Enter a num : "))
         if (y==1):
                  print("Bye from Python program")
                  sys.exit() 
         else:
                  print("y = ", y)
         
print('Outside while loop')#This will not be printed                  
# exit stops the python program execution