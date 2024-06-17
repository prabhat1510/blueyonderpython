# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 10:02:59 2024

@author: UD SYSTEMS
"""

import datetime
from datetime import  timezone 

print("Python current Time example")
ct = datetime.datetime.now()
print ("Current Date and Time :", ct)

print ('Hour:', ct.hour)
print ('Minute :', ct.minute)
print ('seconds :', ct.second)
print(datetime.datetime.now(timezone.utc))#GMT


print(datetime.__doc__)