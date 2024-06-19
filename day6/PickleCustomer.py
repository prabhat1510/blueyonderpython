# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 16:06:34 2024

@author: UD SYSTEMS
"""

from customer import Customer 
import pickle

customerList = list()

while True:
    choice = input('Want to add customer?  Enter Y/N :')
    
    if(choice == 'Y'):
        cId = input('Enter customer id : ')
        cName= input('Enter customer name : ')
        cust = Customer()
        cust.setCustId(cId)
        cust.setCustName(cName)
        customerList.append(cust)
    else:
        break

print(customerList)    
#Opening the file to send the data
pk = open("customerdata1.pickle","wb")

pickle.dump(customerList, pk) #storing the data

pk.close()# closing the file

print("Data is written")



