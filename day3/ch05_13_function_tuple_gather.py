# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 14:52:56 2024

@author: UD SYSTEMS
"""


"""
    Program: ch05_13_function_tuple_gather.py
    Function: Exploring tuple gathering
"""

def simple_function(a, b = "string", *c):
 print("I am from simple_function")
 print("The value of a: ", a)
 print("The value of b: ", b)
 print("The value of c: ", c)
 return

print("\nCalled as simple_function( 10, 'my string', 1, 'astring', 3, 4 )")
simple_function( 10, 'my string', 1, 'a string', 3, 4 )
print("\nCalled as simple_function( 10, 1, 'a string', 3, 4 )")
simple_function( 10, 1, 'a string', 3, 4 )

print("\nCalled as simple_function( 10 )")
simple_function( 10 )

#print("\nCalled as simple_function(10, b='new value', 1, 'astring', 3, 4)")
#simple_function(10, b='new value', 1, 'a string', 3, 4)

print("\nThat's all folks!")