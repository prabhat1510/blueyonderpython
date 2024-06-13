# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 16:26:33 2024

@author: UD SYSTEMS
"""
print("****************Function in Python*********************")
#defined the function using def keyword and name of the function , argument or parameter is optional
#parameter or argument is optional
def printInfo(msg):
    print(msg)
    #return statement optional
#Calling the above defined function
returnMsg = printInfo("Good Morning")
print(returnMsg)

def printInfo(msg):
    print(msg)
    return 

#Call the function

retMsg=printInfo("Subhakar")
print(retMsg)

def display():
    print("Good Evening")

display()

def addition(num1,num2):
    return num1+num2

result = addition(10, 15)
print(result)

result1 = addition('Hello', str(15))
print(result1)

print("**********************************")
def printInfo(fName):
    result=fName+" How are you?"
    return result
x=printInfo("Harshitha")
print(x)

def printInfo(msg):#parameter or argument is optional
    print(msg)
    return  #returning nothing so it will return None
printInfo("Good Evening")
y=printInfo("Good Morning")
print(y)



print("************Functions in Python*****************************")
"""
    Functions are convenient way to divide your code into useful blocks, allowing us to order our code, 
    make it more readable , reuse it and save some time.
     def functionname(parameters):
         
         #Comments or what we call it a DocString
         
         statements
         return [expression] # Its an optional
     
"""

def addWithReturn(a,b):
    """
        This function add two numbers and returns the result to the calling function
    """
    result = a+b
    return result
#Calling a function and assigning the returned value to variable c
c=addWithReturn(10,20)
print(c)
print(addWithReturn.__doc__)
print(str.__doc__)


def addWithOutReturn(x):
    print(x)

result=addWithOutReturn("OOPS")
print(result)

def funcReturnMultiValue():
    num1=15
    num2=18
    return 5,6,7,num1,num2

result3=funcReturnMultiValue()
print(result3)


def funcReturnMultiValue():
    return 5,6,7,"Hello",5.65

result4=funcReturnMultiValue()
print(result4)
print(type(result4))

def addWReturn(a,b):
      """  
          This function add two numbers and returns nothing to the calling function
      """
      print(a+b)
      return  #retunring nothing :- None
c=addWReturn(15,25)
print(c)

def add(a,b):
   '''
        This function add two numbers
   '''
   print(a+b)
     
add(15,25)#Calling a function

print(add.__doc__)
print(addWithReturn.__doc__)
print(addWReturn.__doc__)

def display():
    print("Hello how are you Good Morning")

display()

print("******************************")
foods=["Dosa","Idli","Upma","Vada","Poori","Set Dosa","Sambhar","Chutney","Karam","Koli Butter Masala"]
#forEach()
for food in foods:
    print(food)
else:
    print("No food found")
    
    
#foods.forEach(System.out::println)