# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 11:42:55 2024

@author: UD SYSTEMS
"""

# running simple unix commands 
# system() function is used to run the unix commands from python

import os
print(os.system("date"))

f = os.popen('date')
now = f.read()
print ("Today is ", now)


print(os.system("clear"))

print(os.system("ls"))
print(os.__doc__)
print("###########################")
print(os.curdir)
print("###########################")
print(os.path)
print("###########################")
print(os.name)
print(os.listdir('.'))