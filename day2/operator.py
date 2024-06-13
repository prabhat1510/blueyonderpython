# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 15:34:35 2024

@author: UD SYSTEMS
"""

print("********************Operators**********************")
"""
 Operators in Python 
     These are the contructs which can manipulate the values of the operands.
     2+3= 5  here 2 and 3 are operands and + and = is called operator
     Different types of Operators in Python:
         1. Airthmetic Operators
         2. Assignment Operators
         3. Comparison Operators
         4. Bitwise Operators
         5. Membership Operators
         6. Logical Operators
         7. Identity Operators
"""
print("*************Airthmetic Operators*********************")
a=21
b=10
c=0
c=a+b # + operator adds two operands a and b
print(a+b)
print(21+10)
print(c)
print("**************************************")
c=a-b # - operator subtracts two operands a and b
print(c)
c=a*b # * operator mutliple two operands a and b
print(c)
c=a/b # / operator divides operand a by  b 
print(c)
c=a%b # % operator divides operand a by  b and it returns remainder
print(c)
c=a**b # Exponent ** operator performs exponential (power) calculation on operand a**b ,means a raise to the power b
print(c)

c=a//b #Integer division
print(c)

print("*************************Assignment Operators**************")
m=15 # Assign values from right side operands to left side operand
n=10 # Assign values from right side operands to left side operand
p=m+n
print(p)

#Value of p is 25 and m is 15
p+=m # is equivalent p=p+m
print(p)
p-=m # is equivalent p=p-m
print(p)

p*=m # is equivalent p=p*m
print(p)
p/=m # is equivalent p=p/m
print(p)
p=2
p%=m # is equivalent p=p%m
print(p)
p**=m # is equivalent p=p**m
print(p)

print("*************************Comparison Operators**************")
a=21
b=10
if (a==b):
    print("a is equal to b")
else:
    print("a is not equal to b")
print("**************************")
if a!=b:
    print("a is not equal to b")
else:
    print("a is equal to b")
print("*******************")    
if a>b:
    print("a is greater than b")
else:
    print("a is not greater than b")
print("**************************")    
if a<b:
    print("a is less than b")
else:
    print("a is not less than b")
if(a>=b):
    print("a is greater than or equal to b")
else:
    print("a is not greater than or equal to b")
if (a<b):
    print("a is less than or equal to b")
elif (a==b):
    print("a is equal to b")
else:
    print("a is not less than or equal to b")

print("*******************************************************")
"""
    Binary Numbers, Decimal Numbers,Hexadecimal,Octal Numbers
    bin()
    hex()
    oct()
"""

A=10 #1010
B=7 #0111
print(bin(A))
print(hex(A))
print(oct(A))
print(bin(B))
print("*************************Bitwise Operators**************")
'''
    Binary AND a&b
    Binary OR a| b
    Binary XOR a^b
    Binary Ones Complement ~a
    Binary Left Shift
    Binary Right Shift

'''
a=10 #Binary number of 10 is 1010
b=7 #Binary number of 7 is 0111
print(bin(a))
print(bin(b))
print(hex(a))
print(oct(a))
print("***************")
#AND : returns 1 if both the bits are 1 otherwise 0
'''
    1010
    0111
    -----
    0010   2
'''
print(a&b) #Its returning the decimal of the result after applying and operation on binary numbers a and b

print(bin(a&b))

#OR : returns 1 if any the bits is 1. If both the bits are 0, then it returns 0
'''
    1010
    0111
    -----
    1111   
'''
print(a|b)
print(bin(a|b))

#XOR : returns 1 if  one of the bits  is 0 and the other bit is 1. 
#If both the bits are 0 or 1 , then it returns 0
'''
    1010
    0111
    -----
    1101   
'''
print(a^b)
print(bin(a^b))

#One's complement of a number is equals to -(a+1)
print(~a)
print(bin(~a))

print(~b)
print(bin(~b))

#Binary Left shift operator: It shift the left operand bits towards the left side for the given number of times in the right operand.
print(a<<2) # 0000 0000 0000 1010<<2 = 0000 0000 0010 1000
print(bin(a<<2))

#Binary Right shift operator: Exactly the opposit of the left shift operator. then left side operand bits are move towards the right side for the given number of timers
print(a>>2) # 0000 1010>>2 = 0000 0010
print(bin(a>>2))


print("*************************Logical Operators**************")
'''
    Logical Operators : In python they are used for conditional statements( true or false)
    Three Operators:
        AND, OR , NOT
        
'''
X= True
Y= False
print('X and Y is ', X and Y)
print('X or Y is ', X or Y)
print('not X is ', not X )
print('not Y is ', not Y )
print("*******************************")
if X and Y:
    print("True")
elif X or Y:
    print('X or Y is ', X or Y)
elif not X:
    print('not X is ', not X )
elif not Y:
    print('not Y is ', not Y )
print("*****************************************")


print("*************************Membership Operators**************")
'''
    These operators are used to test whether a value or a variable is 
    found in a sequence (Lists,Tuple,Sets,Strings,Dictionaries) or not.
    Two types of Membership Operators:
    in
    not in 
    
'''
Q=[1,2,3,4,5,6]
Z=3
D=9
print(Z in Q) #true
print(D in Q) #false
print(Z not in Q) #false
print(D not in Q) #true


print("*************************Indentity Operators**************")
'''
    these Operators are used to check if two values (or variables) are located on 
    the same part of the memory.
    Two variables that are equal does not imply that they are identical
    Operators:---
    is 
    is not
    
'''

X1='Welcome to Python'
X2=1234
Y1='Welcome to Python'
Y2=1234
print(X1 is Y1) #True
print(X1 is not Y1) #False
print(X1 is not Y2) #True
print(X1 is X2) #False
print("*******************************")
print(X2 is Y2)
print(X1 is Y1)
print("*******************************")
#verifying using id()
print('Id of X1',id(X1))
print('Id of Y1',id(Y1))
print('Id of X2',id(X2))
print('Id of Y2',id(Y2))


print('************************Conditional Statements or Decison Making*********')
'''
    if elif else
    Syntax:
    if condition1:
        statements
    elif condition2:
        statements
    elif condition4:
        statements
    else:
        statements
'''
X=15
Y=15
if (X<Y):
    print('X is less than Y')
elif X>Y:
    print('X is greater than Y')
else:
    print('X and Y are equal')

    
print("************************Loops******************************************")
"""
     There are two types of loops:
         1. Infintie loop : when condition will never become false
         2.Finite loops : At one point, the condition will become false and 
             the control will move out of the loop.
    There is one more way to categorize loops:-
        Pre test: In this type of loops the condition is first checked and
        then only the control moves inside the loop
           
        Post test: Here first the statements inside the loops are executed, and then the 
        condition is checked
        
        Python does not support Post-test loops
        
        In Python there are three loops:-
        While 
        For
        Nested
"""
#while loop
count=0
while(count<10):
    print(count)
    count=count+1
print("Good Bye!")

while True:
    print(count)
    count=count+1
    if count>20:
        break
print("After Infinite Loop")

"""
    For loop sytanx:
        for each element in a sequence do something
        for variable in sequence:
            statements
"""
print("***********************************For Loops*************************")
fruits=["Mango","Orange","Apple","Banana","Kiwi","Grapes"]
print(fruits)

for fruit in fruits:
    print(fruit)
print("****************")
print(fruits[0])
print(fruits[1])


#for each element in a sequence print element
for fruit in fruits: #for each fruit in fruits 
    print(fruit) #print fruit
    
print("************************************")
for index in range(len(fruits)): #range(start,end,step) default of start is 0 
    print(fruits[index])
    
print("*******************************")
for index in range(1,len(fruits),2): #range(start,end,step) default of start is 0 
    print(fruits[index])    

print("************************************")
myData=[10,5,4,3,7,2,1]
for element in myData:
    print(element)    

print("************************************")
lenOfData=len(myData)
print(lenOfData)
r=range(lenOfData) #start from 0 index and stop at lenOfData i.e. 7
print(r)
r=range(1,lenOfData,3) #start from 1 index and stop at lenOfData i.e. 7
print(r)

for i in r:
    print(myData[i])
    
print("************************************")
print("****************Nested Loop********************")    
myNestedData=[10,5,4,[5,"Mango","Wrangal","Cyberabad"],7,2,[5.64,"Hello"],15]
for elements in myNestedData:
    if type(elements) == list:
        for ele in elements:
            print(ele)
    else:
        print("############")
        print(elements)

print("*****************************break and continue statement*****************")
for val in "string":
    if val=="i":
        break
    print(val)
print("The end")

print("**************Continue******************")
for val in "string":
    if val=="i":
        #print(val)
        continue
    print(val)
print("The end")

