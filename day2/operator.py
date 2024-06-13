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




