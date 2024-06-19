# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 09:55:33 2024

@author: UD SYSTEMS
"""
import re
from customer import Customer
def getCustomerById(cId):
    cust =''
    fo = open('customer.txt','r')
    for line in fo:
         #if(line.split()[0] == str(cId)):
          if(re.match(str(cId),line)):
            cust=line
            break
    return cust


#print(getCustomerById(111))

def getCustomerByName(cName):
    cust =''
    fo = open('customer.txt','r')
    for line in fo:
         if(re.search(cName,line)):
            cust=line
            break
    return cust


#print(getCustomerByName('Marathalli'))


cust = Customer()
cust.setCustId(13)
cust.setCustName('Rahul Kumar')

def updateCustomer(cust):
    fo = open('customer.txt','r+')
    lines = fo.readlines()
    for index in range(0,len(lines)):
        if(re.match(str(cust.getCustId()),lines[index])):
           lines[index]=str(cust.getCustId())+" "+cust.getCustName()+'\n'
           break
    print('---'+str(lines))
    fo.seek(0)
    for line in lines:           
        fo.write(line)
    return "Customer updated successfully"

print(cust)
print(updateCustomer(cust))