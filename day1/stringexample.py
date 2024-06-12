# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 16:11:20 2024

@author: UD SYSTEMS
"""

hello='hello'
print(len(hello))
print(hello.index('l'))
print(hello.count('l'))
print(hello[1:3])
print(hello[::-1])
print("********************************************")
reversedHello = reversed(hello)
print("********************************************")
for rever in reversedHello:
    print(rever)
print("*********************Slicing***********************")
greetings= "Hello How are you ?"
print(greetings[2:])
print(greetings.upper())
print(greetings.lower())
hello="How are you doing ?"
print(hello)
print(hello.index('e'))

print(hello.replace('a','k'))
print(hello)
