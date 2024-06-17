# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 09:58:14 2024

@author: UD SYSTEMS
"""

# Calendar Module

import calendar

# starting day of the week will be sunday
c = calendar.TextCalendar(calendar.SUNDAY) 
c.prmonth(2007, 7) # 2007 july calendar will be printed
c.prmonth(2024, 6)

d = calendar.TextCalendar(calendar.MONDAY)
d.prmonth(2024, 6) 