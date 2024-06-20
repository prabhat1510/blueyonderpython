# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 11:38:46 2024

@author: UD SYSTEMS
"""

listOfNumbers = [2,4,6,8,10]
#result=listOfNumbers/2#TypeError: unsupported operand type(s) for /: 'list' and 'int'
#print(result)

import array as arr
import numpy as np
#a = arr.array("i",listOfNumbers)
#print(a/2)
ares = np.array(listOfNumbers)
print(ares/2)

#print(np.__doc__)

myArr= np.array([1,2,3,"Sujan",5.6])
print(myArr)
print(type(myArr))


myArray=arr.array("b",[1,2,3,127])
print(myArray)
print(type(myArray))

myArray=arr.array("u",["$","/"])
print(myArray)
print(type(myArray))


myListArr=[1,2,3,4]
ar= np.array(myListArr)
divC=ar/3
print(divC)
'''
    [[1,2]
    [3,4]]
'''
my2DArr = [[1,2],[3,4]]
'''
    [
         [
             [1, 2], [3, 4]
        ], 
         [
             [5, 6], [7, 8]
        ]
    ]
    
'''
my3DArr = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
a2D = np.array(my2DArr)
print(a2D)

a3D = np.array(my3DArr)
print(a3D)

print(a2D.size)
print(a3D.size)
print("*******************************************")
for i in range(len(a2D)):
    for j in range(len(a2D[i])):
        print(a2D[i][j])
print("*******************************************")
for element in a2D:
    print(element)
    
print("*******************************************")

for i in a2D:
    for j in i:
        print(j)
        
print("******************Add Two Matrix*************************")

matA = [[1,2,3],[4,5,6],[7,8,9]]
matB = [[1,2,3],[4,5,6],[7,8,9]]

arrA = np.array(matA)
arrB = np.array(matB)

print(np.add(arrA,arrB))
print(np.add(matA,matB))
print(np.multiply(arrA,arrB))
print(np.transpose(matA))
print("*********************************************************")

print(np.add(5,10))
print(np.multiply(5,10))
print(np.cos(0))
print(np.sin(90))
print(np.log10(10))
print(np.log(10))
print(np.log(2))
print(np.log2(2))