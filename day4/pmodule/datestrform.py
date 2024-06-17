# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 10:16:48 2024

@author: UD SYSTEMS
"""

# datetime module

import datetime
print("Printing Date in different formats")

t1 = datetime.date(2015,6,30)
print ("Current date", t1)

print(t1.strftime("%d-%m-%Y"))  # 30-06-2015
print(t1.strftime("%d-%B-%Y"))  # Month name in fullname format 30-JUNE-2015
print(t1.strftime("%d-%b-%Y")) # Month name in 3 letter format  30-JUN-2015
print(t1.strftime("%A,%d-%b-%y")) # date will printed with week day TUESDAY, 30-JUN-2015

date1 = datetime.date(2015,6,30)
print ("Current date", date1)

date2 = datetime.date.today()
print ("Today's date", date2)

print(date1>date2)
print(date1<date2)
print(date1-date2)

