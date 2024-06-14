# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 10:08:51 2024

@author: UD SYSTEMS
"""

print('*******************************************')

a=10
b=11
c='efg'
d='abc'

def doSomething(x,y):
    return x+y # + is polymorphic

print(doSomething(a,b))
print(doSomething(c,d))
print(a,"---value--- ",b)
if(a ==10):
    a=15
    b=11
    print(a,"---value--- ",b)

print(a,"---value--- ",b) 

a=25
b=21   
print(a,"---value--- ",b) 