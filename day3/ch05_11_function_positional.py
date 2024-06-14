# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 14:48:27 2024

@author: UD SYSTEMS
"""

"""
    Program: ch05_11_function_positional.py
    Function: Exploring positional passing
"""

def simple_function(a, b, c=15):
 print ("I am from simple_function")
 print ("The value of a: ", a)
 print ("The value of b: ", b)
 print ("The value of c: ", c)
 return

print ("\nCalled as simple_function( 10, 'my string', 344.1)")
simple_function( 10, 'my string',344.1 )

print ("\nThat's all folks!")

simple_function( 10, 'my string' )