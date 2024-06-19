# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 16:06:34 2024

@author: UD SYSTEMS
"""

from customer import Customer 
import pickle

customerList = list()
cust = Customer()
while True:
    choice = input('Want to add customer?  Enter Y/N :')
    
    if(choice == 'Y'):
        cId = input('Enter customer id : ')
        cName= input('Enter customer name : ')
        cust.setCustId(cId)
        cust.setCustName(cName)
        customerList.append(cust)
    else:
        break
    
#Opening the file to send the data
#pk = open("customerdata.pickle","wb")

#pickle.dump(customerList, pk) #storing the data

#pk.close()# closing the file

#print("Data is written")



pkRead = open("customerdata.pickle","rb") # opening the file

listOfCustomer = pickle.load(pkRead) #reading the data

print(listOfCustomer) #printing the output

for c in listOfCustomer:
    