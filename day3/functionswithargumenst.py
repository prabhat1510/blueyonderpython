# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 14:13:10 2024

@author: UD SYSTEMS
"""

print("*****************************Functions arguments ***********************")
"""
    You can call a function by using the following types of formal arguments
    1. Required arguments
    2. Keyword arguments
    3. Default arguments
    4. variable Length Arguments
           
"""

print("*****************************Required arguments ***********************")
def printMe(msg):
        """
            This prints a passed string into this function
        """
        print(msg)

printMe("Hello")
#TypeError: printMe() missing 1 required positional argument: 'msg'
#printMe()

def printMe(msg,msg2):
        """
            This prints a passed string into this function
        """
        print(msg+msg2)

printMe("Hello","Good Morning")
#TypeError: printMe() missing 1 required positional argument: 'msg2'
#printMe("Hello")

print("*****************************Keyword arguments ***********************")

def printMe(msg):
        """
            This prints a passed string into this function
        """
        print(msg)

printMe(msg="Hello")#Keyword is msg. 

def printMe(msg,msg2):
        """
            This prints a passed string into this function
        """
        print(msg+msg2)

printMe(msg="Hello",msg2="Good Morning")
printMe(msg2="Hello",msg="Good Morning")
printMe("Hello",msg2="Good Morning")

#SyntaxError: positional argument follows keyword argument
#printMe(msg="Hello","Good Morning")

print("*****************************Default arguments ***********************")

def printInfo(name,age=18):
    """
        This prints a passed info into this function
    """
    print("Name: ",name)
    print("Age: ",age)

printInfo("India")
printInfo("India",age=20)#age=20 is overriding the default value of age
printInfo(name="Indira",age=65)

print("*****************************Variable-length arguments ***********************")
def printInfo(arg1,*varArg):
    """
        This prints a variable passed arguments
    """
    print("Agr 1 is : ",arg1)
    print("*****varArg*******",*varArg)
    print(type(varArg))
    for element in varArg:
        print(element)
printInfo(15)
printInfo(15,70,80,90,40,50,30,20,10)

print("***************************** **kwargs arguments ***********************")

def printWords(arg1,**kwargs):
    print("Agr 1 is : ",arg1)
    print("*****kwargs*******",kwargs)
    print(type(kwargs))


#printWords(arg1="Hi",h='Hello',bye='Bye!!')
printWords('Hi',name="Alice", age=25, city="Paris")
printWords('Hi',h1="Alice", h2=25, h3="Paris")