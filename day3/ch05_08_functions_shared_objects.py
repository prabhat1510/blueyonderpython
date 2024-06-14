# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 11:46:14 2024

@author: UD SYSTEMS
"""


"""
    Program: ch05_08_functions_shared_objects.py
    Function: This is a contrived function but does show how mutable
    and immutable object passing work
"""

def add_10(add_10_immutable,add_10_mutable):
        print("add_10_mutable is mutable")
        print("add_10_mutable == mutable")
        add_10_immutable +=10
        print("Inside add_10")
        print("            immutable object   =",add_10_immutable)
        #for i in range(len(add_10_mutable)):
         #   add_10_mutable[i] += 10
        add_10_mutable = [ x + 10 for x in add_10_mutable]
        print("    Local mutable object = ",add_10_mutable)
        #return 
        return add_10_mutable    

immutable = 10
mutable = [1,2,3] #list which is mutable

print("Outside add_10")
print("     immutable object value= ", immutable)
print("     mutable object value= ", mutable)
#add_10(immutable,mutable)
mutable = add_10(immutable,mutable)
print("Outside add_10")
print("     immutable object value= ", immutable)
print("     mutable object value= ", mutable)
