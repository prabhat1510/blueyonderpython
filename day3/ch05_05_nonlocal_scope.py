# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 11:06:34 2024

@author: UD SYSTEMS
"""
#SyntaxError: nonlocal declaration not allowed at module level
#nonlocal oct
def outer_function():
    #SyntaxError: no binding for nonlocal 'oct' found
    #nonlocal oct
    oct = 10#3
    print("oct in outer_function 1 =", oct)#4

    def inner_function():
        nonlocal oct #inside nested function
        oct = 'ABC'#6
        print("oct in inner_function =", oct)#7

    inner_function()#5
    print("oct in outer_function 2 =", oct)#8

# start of main code
oct = 0 #1
print("oct in module before =", oct) #2
outer_function()#2
print("oct in module after =", oct)#9
print("That's all folks!")#10