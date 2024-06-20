# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 09:47:52 2024

@author: UD SYSTEMS
"""
vowels=("a","e","i","o","u","o")
fset1=frozenset(vowels)
print("Frozen set is:",fset1)
print(type(fset1))
print("Empty Frozen set is:",frozenset())

person={"name": "John", "age": 23, "sex": "male"}
fSet2 = frozenset(person)
print('The frozen set is:', fSet2)

print(person.keys())
print(fset1 & fSet2) #Intersection In this example there is no common element so empty frozen set will be returned
print(fset1 | fSet2) #Union


listOfNumbers=[5,4,3,2,10,11]
listOfNums=[4,1,5,6,8]
fSetListOfNumbers = frozenset(listOfNumbers)
fSetListOfNums = frozenset(listOfNums)

print(fSetListOfNumbers & fSetListOfNums)
print(fSetListOfNumbers | fSetListOfNums)
print(fSetListOfNumbers.difference(fSetListOfNums))
print(fSetListOfNums.difference(fSetListOfNumbers))
print(fSetListOfNumbers.symmetric_difference(fSetListOfNums))
print(fSetListOfNumbers.union(fSetListOfNums))
print(fSetListOfNumbers.intersection(fSetListOfNums))


