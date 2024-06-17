# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 14:19:20 2024

@author: UD SYSTEMS
"""
from passwordmismatchexception import PasswordMismatchException
from usernamenotfoundexception import UserNameNotFoundException

def login(username,password):
    uname="Bill"
    passw='1234'
    if(uname == username):
        if(passw == password):
            return 'Login Successfully'
        else:
            raise PasswordMismatchException("Passowrd is not correct for " + username)
    else:
        raise UserNameNotFoundException('Username '+username+ ' dosen\'t exist')        