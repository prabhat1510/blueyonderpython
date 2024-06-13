# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 10:28:42 2024

@author: UD SYSTEMS
"""

"""
 List is a mutable object   
 It containes elements of different datatype inside a square bracket with 
 comma separated values
"""
mList=[]#empty list
myList=[4,2,7,8,10] #list containing numbers
mListMix=[4,2,7.65,8,10,"Hello",5,1,15,2,5] #list containing mix data type elements

print(type(mList))
print(type(myList))
print(type(mListMix))

print(len(mList))
print(len(myList))
print(len(mListMix))

print(mListMix[7])
print(mListMix[2:7])#start : end-1
print(mListMix[::-1]) #slicing operator list elements are reversed
print("*********************************************")

print(mListMix)
print(mListMix.reverse()) #doesn't return anything
print(mListMix)

print("*********************************************")
mListMix[2]=9.86
print(mListMix)
print("*********************************************")
print(dir(mListMix))
print(mListMix.count(5))
print(mListMix.index(7.65))
print("*********************pop function************************")
print(mListMix)
print(mListMix.pop()) #By default it will remove the last element of the list
print(mListMix.pop(2)) #It will remove the element placed at index position passed in pop function
print(mListMix)
print("*********************remove function************************")
print(mListMix.insert(1, 7.65))
print(mListMix)
print(mListMix.remove(7.65)) #it will remove the element passed an argument to the function and will return none
print(mListMix)
print("*********************sort function************************")
#We have mix data type elements so it will throw an error
#print(mListMix.sort()) #TypeError: '<' not supported between instances of 'str' and 'int'
print(myList)
print(myList.sort()) # not returning anything its making changes in the same object
print(myList)
print(myList.sort(reverse=True))#it will sort in descending order as reverse=True
print(myList)
print("**************copy function******************")
print(mList)
mList=[4,2.1,7.5,8,10]
cList=mList.copy() #It creates a copy of a list
mList.sort() #By default it will sort in ascending order
print(mList)
print(type(cList))
print(cList)
cList[3]=15
print(cList)
print(mList)
print("**************sort function on strings******************")
sList=["Hello","Abc","def","abc","mno"]
sList.sort()
print(sList)
sList.sort( reverse=True)
print(sList)
print("**************clear function ******************")
print(cList)
print(mList)
print(cList.clear())
print(cList)
print("**************************insert*****************************")
mList.insert(2,"Hello")#it insert an element at the given index position
print(mList)
mList.insert(3,"BlueYonder")
print(mList)
print("*****************************append and extend****************")
nList=[4,2.1,8,10]
nList.append(20)
print(nList)
nList.append([15,16,17]) #It will create a nested list i.e. a list inside a list [4, 2.1, 8, 10, 20, [15, 16, 17]]
print(nList)
#nList.append(15,16,17)#TypeError: list.append() takes exactly one argument (3 given)
#nList.extend(151) #TypeError: 'int' object is not iterable
nList.extend([1,5,1,11,14,18])
print(nList)
nList.extend(["Hello",20,21,'Will take break in few minutes'])
print(nList)
nList.extend([151,151,151])
print(nList)
print("****************************************************")
rList=[2,2,4,6]
print(rList)
for index in range(len(rList)):
    if rList[index] == 2:
        rList[index] = 8
print(rList)
print("****************************************************")
for element in rList:
    print(rList)
print("****************************************************")
del rList[1]
print(rList)

del rList
#print(rList)
