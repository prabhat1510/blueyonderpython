# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 10:12:35 2024

@author: UD SYSTEMS
"""
x=[1,2,4,5.6,'Hi']
a = list()
a=[]
for i in range(10):
        a=[i]+a
print(a)
print(type(a))

'''
Lists and np.array both support having elements 
of different data structure. 
Whereas, the arrays from array module supports data 
only of the same data type.

'''
import numpy as np
arr = np.array([1,2,3.0,"hello"])
print(arr)
print(type(arr))
print(arr[0])

for a in arr:
    print(a)

import array as ar
arrElements = ar.array("i",[1,2,3])
print(arrElements)
print(type(arrElements))

#Type Code u refers to unicode_character in Python
arrElements = ar.array("u",['H','o','w'])
print(arrElements)
a1 = ar.array('l')
a2 = ar.array('u', 'hello \u2641')
a3 = ar.array('l', [1, 2, 3, 4, 5])
a4 = ar.array('d', [1.0, 2.0, 3.14])
print(a1)
print(a2)
print(a3)
print(a4)










