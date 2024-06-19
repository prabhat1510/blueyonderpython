# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 16:50:15 2024

@author: UD SYSTEMS
"""

import pickle

pkRead = open("customerdata1.pickle","rb") # opening the file

listOfCustomer = pickle.load(pkRead) #reading the data

#print(listOfCustomer[0].getCustId()) #printing the output
pkRead.close()
for c in listOfCustomer:
    print(str(c.getCustId()) +" "+ c.getCustName())    