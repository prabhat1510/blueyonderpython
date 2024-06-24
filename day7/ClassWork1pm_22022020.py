# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 14:35:27 2020

@author: Admin
"""

a=[]
for i in range(10):
        print([i])
        a=[i]+a
        print(a)
print(a)
print(type(a))

import numpy as np

myArr= np.array([1,2,3,"Sujan",5.6])
print(myArr)
print(type(myArr))

import array as arr
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


#Accessing the list
#Emplty list
my_list=[]
print(my_list)
#list of integers
my_list=[1,2,3]
print(my_list)

#list with mixed datatypes
my_list=[1,"Hell",3,4.5]
print(my_list)

#nest list
myNestedList=["mouse",[8,4,6],["a"]]

print(myNestedList[1][1])
print(myNestedList[2][0])
print(myNestedList[1:3])

odd = [1, 3, 5]
odd.append(7)
print(odd)
odd.append(my_list)
print(odd)
print(len(odd))
print("***********************")
odd.extend(my_list)
print(odd)
print(len(odd))

even = [2, 4]
result=even+[6,8,10]
print(result)

even.insert(0,5)
print(even)
even.insert(0,result)
print(even)
even[2:4]=[7,11,10,9]
print(even)
even.insert(1,34)
print(even)
even[1]=420
print(even)
even[0][1]=415
print(even)



my_list = ['p','r','o','b','l','e','m']
"""
del my_list[2]
print(my_list)
del my_list[1:3]
print(my_list)
del my_list
"""
my_list.remove("o")
print(my_list)
my_list.pop()
print(my_list)
print(my_list.pop(2))
print("*****************")
print(my_list)
print(my_list.clear())
print(my_list)

myDiffList=[3,8,1,6,"Hello",0,8,"Abc",4]
myList=[3,8,1,6,0,8,4]
print(myList.index(6))
print(myList.index(8))

for i in range(len(myList)):
    if myList[i] == 8:
        print(i)
        
print(myList.count(8))
print(myList.reverse())
print(myList)
print(myList.sort())
print(myList)
print("*********************")
copiedList=myList.copy()
print(copiedList)
myDiffList.sort(key=str)
print(myDiffList)

pow2=[2**x for x in range(10) ]
print(pow2)
pow2=[2**x for x in range(10) if x > 5]
print(pow2)

odd = [x for x in range(20) if x % 2 == 1]
print(odd)




