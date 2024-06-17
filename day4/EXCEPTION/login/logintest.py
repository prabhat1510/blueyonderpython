# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 14:24:56 2024

@author: UD SYSTEMS
"""
from login import login
from passwordmismatchexception import PasswordMismatchException
from usernamenotfoundexception import UserNameNotFoundException

username = input('Enter username : ')
password = input('Enter password: ')

try:
    msg = login(username,password)
    print(msg)
except UserNameNotFoundException as u:
    print(f'{u}')

except PasswordMismatchException as p:
    print(f'{p}')