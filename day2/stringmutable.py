# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 10:38:21 2024

@author: UD SYSTEMS
"""

greetings= "Hello How are you All ?"
#greetings[3]='S'#TypeError: 'str' object does not support item assignment
print(greetings)
greetings="Good Morning"
print(greetings)
print('************************')
greetings =greetings.replace('o', 'S')
print('************************')
print(greetings)
print(greetings.index('d'))
print(greetings[3])
print(dir(greetings))