# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 15:57:34 2024

@author: UD SYSTEMS
"""

def sum(x,y):
    return x+y

result= sum(15,10)
print(result)

print("*************Using Lambda Function*****************")

add = lambda x,y:x+y
res = add(1,2)
print(res)

print(add(5,10))

#isEligibleVote = lambda age : if age<18 print('Not Eligible')
#print(isEligibleVote)
#print(isEligibleVote(21))

results = lambda x,y : f"{x} is smaller than {y}" if x < y else (f"{x} is greater than {y}" if x>y  else f"{x} is equal to {y}")
print(results(11,10))

print("**************************************************")
list1 = [1, 2, 3, 4, 5]
#r= lambda x: [print(f' {x}') for x in list1]
r= lambda x: [print(f' {x}') for x in list1]
r(list1)


print("**********************For tuple****************************")
tup1 = (1, 2, 3, 4, 5)
r= lambda x: [print(f' {x}') for x in tup1]
r(tup1)

print("**********************For tuple without print****************************")
tup1 = (1, 2, 3, 4, 5,6,7,8,9,10)
odd= lambda x: [f' {x}' for x in tup1 if (x%2 != 0)] 
lodd= list(odd(tup1))
print(lodd)

tup12 = (1, 2, 3, 4, 5,6,7,8,9,10)
even= lambda x: [f' {x} is even' if (x%2 == 0) else (f' {x} is odd') for x in tup12 ]
leven= list(even(tup12))
print(leven)