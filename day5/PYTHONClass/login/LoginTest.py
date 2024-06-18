# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 16:21:36 2024

@author: UD SYSTEMS
"""
#from Login import Login
from LoginService import LoginService

from passwordmismatchexception import PasswordMismatchException
from usernamenotfoundexception import UserNameNotFoundException

uName = input('Enter username : ')
passwd = input('Enter password: ')
'''
login = Login()
login.setUserName(username)
login.setPassword(password)
'''
msg=''
try:
    msg = LoginService.verifyUserNameAndPassword(uName,passwd)
    print(msg)
except UserNameNotFoundException as u:
    print(f'{u}')

except PasswordMismatchException as p:
    print(f'{p}')
    
if(msg == 'Login Successfully'):
    print(uName)
    #print('harshitha')
    #print('Medahalli')
else:
    print(msg)

