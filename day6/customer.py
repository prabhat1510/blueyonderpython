# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 09:38:37 2024

@author: UD SYSTEMS
"""

class Customer:
    #Class level variable is similar to static variable
    #city='Bengaluru'
    
    def getCustId(self):
        return self.__custId_ #instance variable __custId_ which is a private
    def getCustName(self):
        return self.__custName_
    def setCustId(self,cId):
        self.__custId_=cId
    def setCustName(self,cName):
        self.__custName_=cName
    
    