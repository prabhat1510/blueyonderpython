# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 16:03:30 2024

@author: UD SYSTEMS
"""

class Login:
    
    def __init__(self):
        self.__userName_=''
        self.__password_=''
        
    def getUserName(self):
        return self.__userName_
    
    def setUserName(self,uName):
        self.__userName_=uName
        
    def getPassword(self):
        return self.__password_
    def setPassword(self,passwd):
        self.__password_=passwd

