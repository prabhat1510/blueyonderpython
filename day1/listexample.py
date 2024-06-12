# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 15:35:26 2024

@author: UD SYSTEMS
"""

subjects =['Physics','Chemistry','Maths',2]
print(type(subjects))
print(subjects)

print(subjects[0])
print(subjects[1])
print(subjects[2])
print(subjects[3])
#print(subjects.__length__())
print(len(subjects)) #len function or method is present
s='Physics'
print(len(s))#len function or method is present
print("***************************************")
for subject in subjects:
    print(subject)

print("***************************************")
for i in range(0,len(subjects)):
    print(subjects[i])
    
print("***************************************")
lengthOfSubjects =len(subjects)
index=0
while(index<lengthOfSubjects):
    print(subjects[index])
    index+=1

print("*****************slice**********************")
print(subjects[1:3])
print("*****************slice**********************")
print(subjects[1:])

print("***************************************")

# List creation
empList = [ 2001, 'Shivani',2005, 'Sanjay', 2007, 'Babu']
print ("employee Details : \n", empList)

#specific element from List - Indexing
print("2nd Position : ", empList[1])

#printing Range of element - Slicing
print("1st to 4th element : ", empList[0:4])

#printing from 2nd element to last element
print("2nd to last element : ", empList[1:])
      
#printing the list two times - Repeation
print(empList*2)

print("***************************************")
listOfNumbers = [2,4,3,1,5,6,8,9]
del listOfNumbers[2]
print(listOfNumbers)
listOfNumbers[1]=6
print(listOfNumbers)