# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 12:45:33 2024

@author: UD SYSTEMS
"""

setOfNumbers={15,10,11,12,16}
print(type(setOfNumbers))
print(setOfNumbers)
setOfNum=set()
listOfNum=list()
tupleOfNum=tuple()
#tupleOfNum[0]=11
print(tupleOfNum)
setOfWords={'Hi','Hello','Bye','Hi'}
print(setOfWords)
    
print("****************************Set Objects********************") 
setA = {1, 2, 3}
print(type(setA))  
setB = { 3,3,4,1, 2,5,6}
print(type(setB))  
print(setB)          
setMixData={1, 2.65, 3,"Hello"}
print(type(setMixData))  
print(setMixData) 

#Union of two sets
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print ( A | B)

#Intersection of two sets
print ( A & B )

C={'Hi','Hello','HI','Bye'}
D={'Hi','BYE','Good'}
print ( C & D )

#difference of two sets
A = {1, 2, 3, 4, 5}
B = {1,2,3,4, 5, 6, 7, 8}
print(A - B)
print(B - A)

#Symmetric difference
B = {4, 5, 6, 7, 8}
print(A ^ B)

print(dir(A))
print("********************************************************")

A = {1, 2, 3, 4,5}
B={2, 3,5}
print(A.issubset(B))
print(B.issubset(A))
print(A.issuperset(B))
print(A.union(B))
print(A.intersection(B))
print(A.difference(B))
print(B.difference(A))

B.add(15)
print(B)
listOne=[15,10,9]
myset=set(listOne)
print(myset)
myset.update([8,6,4,2])
print(myset)

myset.update([8.6,6.2,4.1,2.2],{1, 4})
print(myset)
print(len(myset))

#TypeError: 'set' object is not subscriptable
#print(myset[11])
for e in myset:
    print(e)
print("*************************************************************")
print(myset)
print(myset.pop())
print(myset.pop())
print(myset)
print(myset.remove(8.6))
print(myset)
