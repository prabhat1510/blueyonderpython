# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 12:38:19 2024

@author: UD SYSTEMS
"""

def isEligibleToVote(actualAge,defaultAge=18):
    print(actualAge," + ",defaultAge)
    if(actualAge == 18):
        print('Eligible to vote')
    elif(actualAge > 18):
        print('Eligible to vote')
    elif(defaultAge == 18):
        print('Eligible to vote')
    else:
        print('Not Eligible to vote')        
        
isEligibleToVote(21)
#isEligibleToVote() #Error
#isEligibleToVote('Hi') #Error
isEligibleToVote(11,11)
isEligibleToVote(11)

print("********************************")
#Variable arguments in Python Function
def sf(num,num1,*p):
    print(num)
    print(num1)
    print(p)
    #p[3]=6
    
#sf(1,11,10,12,15,16)
#sf(1,11,[10,12,(1,2,3),15,16],111)
sf(1,2)

print("********************************")
#**kwargs -- Keyword Arguments in Python Function
def sfd(x,y,z,a,b,**p):
    print(x)
    print(y)
    print(z)
    print(a)
    print(b)
    print(p)

#sfd(15,16,18,19,110,111,11111,155555)
sfd(15,16,18,19,110,key1=111,key2=11111,key3=155555)

#sf(15,16,key1=111,key2=11111)