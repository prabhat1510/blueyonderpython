# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 12:02:57 2024

@author: UD SYSTEMS
"""
'''
    Tuple is immutable
'''
chelsea = ('Hazard','Lampard','Henry',15,'Lampard')
print(chelsea)
print(type(chelsea))
print(dir(chelsea))
print(chelsea.count('Lampard'))
print(chelsea.index('Lampard'))
print(chelsea.index(15))
weekdays=('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday')
print(weekdays[2])
#weekdays[2]='Funday'#TypeError: 'tuple' object does not support item assignment
#print(weekdays[2])
print(weekdays.__dir__)
print(weekdays.__dir__())
print(weekdays.__len__())
print(weekdays.__ne__(2))
print(weekdays.__getitem__(1))
print(weekdays.__getitem__(4))

numbers=(11,15,14,10,9,25,6,10)
print(12 in numbers)
print(15 in numbers)
print(len(numbers))
print(min(numbers))
print(max(numbers))
print(numbers.count(10))
print(numbers.count(11))
print(numbers.index(10))
print(numbers[1:4])
print(numbers[1:5:2])
print(numbers*4)
#print(numbers+115)#TypeError: can only concatenate tuple (not "int") to tuple
print(numbers+(115,114,110))

#print(chelsea.__reduce__())#pickle serialization and deserialization