# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 15:06:24 2024

@author: UD SYSTEMS
"""

"""
    Program: ch05_17_pass_sequence.py
    Function: Exploring sequence expansion
"""

def simple_function(a, b):
 print("I am from simple_function")
 print("The value of a: ", a)
 print("The value of b: ", b)
 return

s1 = ('a15', 'b15')
print("\nCalled as simple_function( *s1)")
simple_function( *s1)

s1 = ['a11', 'b11']
print("\nCalled as simple_function( *s1)")
simple_function( *s1)

print("\nThat's all folks!")