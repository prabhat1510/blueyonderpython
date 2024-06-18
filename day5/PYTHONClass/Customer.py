# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 15:01:08 2024

@author: UD SYSTEMS
"""

class Customer:
    #By Default class variables or members are public in Python. We can access these variables using className.variableName
    #custId=0
    #custName=''
    #city=''
    
    def __init__(self,cId,cName,city):
        self.__custId_=cId
        self.__custName_=cName
        self.__city_=city
        
    def getCustId(self):
            return self.__custId_
    
    def getCustName(self):
            return self.__custName_
    
    def getCity(self):
            return self.__city_
    
    def setCustId(self,cId):
            self.__custId_=cId
    
    def setCustName(self,cName):
            self.__custName_=cName
    
    def setCity(self,city):
            self.__city_=city
            
            
listOfCustomers=list()
try:
    while True:
        choice = input("Want to enter customer details Y/N: ")
        if choice == 'Y':
            cId=int(input('Enter customer  id  : '))
            cName=input('Enter customer name : ')
            city=input('Enter city : ')
            customer =Customer(cId,cName,city)
            listOfCustomers.append(customer)
        else:
            break
        
except ValueError:
        print("Enter appropriate value")
        
print(listOfCustomers)
print("***********************************************")
for cust in listOfCustomers:
    print(str(cust.getCustId())+" *** "+cust.getCustName()+" *** "+cust.getCity())
    
print("******************setting new values*****************************")
for cust in listOfCustomers:
    cust.setCity('Bengaluru')
    
print("**********************getting updated data*************************")
for cust in listOfCustomers:
    print(str(cust.getCustId())+" *** "+cust.getCustName()+" *** "+cust.getCity())

print('************************Accessing class variables******************************')
#By Default class variables or members are public in Python. We can access these variables using className.variableName
#print(Customer.city)
#print(Customer.custId)
#print(Customer.custName)    