# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 15:29:21 2024

@author: UD SYSTEMS
"""

class Customers:
    '''
    def __init__(self):
        self.__custId_=0
        self.__custName_=''
        self.__city_=''
    '''    
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
            #customer =Customer(cId,cName,city)
            customer= Customers() #Creating an object by calling constructor
            customer.setCustId(cId)
            customer.setCustName(cName)
            customer.setCity(city)
            listOfCustomers.append(customer)
        else:
            break
        
except ValueError:
        print("Enter appropriate value")
        
print(listOfCustomers)
print("***********************************************")
for cust in listOfCustomers:
    print(str(cust.getCustId())+" *** "+cust.getCustName()+" *** "+cust.getCity())
