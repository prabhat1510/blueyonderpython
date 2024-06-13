# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 14:29:15 2024

@author: UD SYSTEMS
"""

employee ={
	"empname": "charisma",
	"empId": 1234,
	"dept": "IT Delivery"
}
print(employee)
print(employee["empname"]) #accessing the element
print(employee.keys())
print(employee.items())
print(employee.get("dept"))# access the element using key
print(employee.values())
#print(employee.update())
employee.setdefault("city","Bengaluru")
print(employee)
employee.update({"street":"bellandur"})
print("****************************************************")
print(employee)
employee.update({"city":"Chennai"})
print(employee)
employee.update({"houseNo":"1510"})
print(employee)
print("****************************************************")
employee.setdefault("city","Hyderabad")
print(employee)

print("******Remove duplicates from a list using dictionary*****************")

#How to remove the duplicates from a list using dictionary
mListData=[5,7,8,"hello",5.6,5,"hello",15]

#Below fromkeys function is creating a key value pair from the list
q=dict.fromkeys(mListData)
print(q)
print(list(q))

d =dict(zip(mListData,mListData))
print(d)
print(list(d))

#Using set remove duplicates 
s=set(mListData)
print(s)
print(list(s))

mDict={'Name': 'Rishi', 'Age': 23, 'Address': 'Vizag','Address': 'HYD','Name': 'Raman','city':'Begumpet'}
print(mDict['Name'])
print(mDict.get('Name'))

print("***************Dictionary Operations**********************")
print(mDict.items())

print(mDict.keys())
print(list(mDict.keys()))
print(mDict.pop("Age"))
print(mDict)
print(mDict.get("Address"))
print("**************************")
print(mDict)
print(mDict.popitem())#remove the last key value pair
print(mDict)
print(mDict.clear())
print(mDict)


