# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 12:52:12 2024

@author: UD SYSTEMS
"""

from customernotfoundexception import CustomerNotFoundException

def findCustomerById(custId):
    if(custId == 15):
        print(f'Customer with {custId} exist')
    else:
        raise CustomerNotFoundException('Customer with ' + str(custId) +' doesn\'t exist')

