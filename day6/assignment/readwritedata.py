# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 09:37:30 2024

@author: UD SYSTEMS
"""
from customer import Customer


cust = Customer()
fo=''
def readCustomerData():
    cId = input('Enter customer id ')
    cName = input('Enter customer name ')
    cust.setCustId(cId)
    cust.setCustName(cName)
    return cust


try:
    cust=readCustomerData()
    fo = open('customer.txt','a+')
    fo.write(cust.getCustId()+" "+cust.getCustName()+'\n')
except FileNotFoundError:
    print('File doesn\'t exists')
finally:
    fo.close()
    

