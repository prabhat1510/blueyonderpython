# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 11:54:07 2024

@author: UD SYSTEMS
"""

# Example for finding the simple interest

import constantp   # adding the module with constant values


p=float(input("Enter the Principle amount :"))
term=int(input("Enter the term :"))

#Example 1
si=(p*term*constantp.roi)/100
print("Simple Interest 1:", si)

#Example 2
si=(p*term*constantp.roi1)/100
print("Simple Interest 2:", si)


#Example 2
constantp.roi1=20.00
si=(p*term*constantp.roi1)/100
print("Simple Interest 2:", si)
