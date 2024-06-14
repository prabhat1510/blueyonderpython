# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 10:58:04 2024

@author: UD SYSTEMS
"""

global oct
def outer_function():
    #global oct#3
    oct = 10
    print("oct in outer_function 1 =", oct)#4

    def inner_function():
        #oct = 'ABC'#6
        print("oct in inner_function =", oct)#7

    inner_function()#5
    print("oct in outer_function 2 =", oct)#8

# start of main code
#global oct #1
oct = 110
print("oct in module before =", oct) #2
outer_function()#2
print("oct in module after =", oct)#9
print("That's all folks!")#10