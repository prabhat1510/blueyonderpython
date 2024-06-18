# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 16:07:53 2024

@author: UD SYSTEMS
"""
#from Login import Login
from passwordmismatchexception import PasswordMismatchException
from usernamenotfoundexception import UserNameNotFoundException

class LoginService:
    
    def verifyUserNameAndPassword(uName,passwd):
        if(uName != str('') and passwd != str('')):
            if(uName == 'user'):
                if(passwd == 'password'):
                    return "Login Successfully"
                else:
                    raise PasswordMismatchException('Please enter valid password')
            else:
                raise UserNameNotFoundException('User name '+uName+' doesn\'t exist')
        else:
            return 'Please enter username and passowrd'