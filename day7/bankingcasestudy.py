# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 12:49:29 2024

@author: UD SYSTEMS
"""

import os
import sys
from datetime import datetime, date
from typing import List
import matplotlib.pyplot as plt
import matplotlib.style as stl
stl.use('ggplot')


def Create_Account():
      global Acc_no, Acc_name, Acc_type, Acc_address, Amount_deposit,dict1, list1, tuple2, list2
 

  
   
      Acc_no = int(input("Account Number: "))
      Acc_name = input("Account holder name: ")
      Acc_type = input("Type of Account[Current/Savings] ")
      Acc_address = input("Account holder address: ")
      Amount_deposit = int(input("Enter the amount to be deposited: "))
      print("Customer Account Created Successfully")
        
      list2=[Acc_no]
      tuple2=(list2)
      list1= []
      list1.append(Acc_name)
      list1.append(Acc_type)
      list1.append(Acc_address)
      list1.append(Amount_deposit)
    
      dict1 = {}
      dict1[Acc_no]=list1
        
                
   
        
      file=open("D:\\accdemo.txt","a")
      file.write("Customer Information \n")
      file.write("******************** \n")
      file.write("Account No: %d\n" %Acc_no)
      file.write("Account Holder Name: %s\n" %Acc_name )
      file.write("Account Type: %s\n" %Acc_name)
      file.write("Account Holder Address: %s\n" %Acc_address)
      file.write("Balance: %d\n" %Amount_deposit)
      intro()
        
        
def View_AccountDetails():
    print("Customer Information\n")
    print("********************\n")
    Acc_no=int(input("Enter your Account Number: \n"))
    if Acc_no in list2:
        values = dict1[Acc_no]
        print("Name:",values[0])
        print("Account Type: ", values[1])
        print("Address: ", values[2])
        print("Balance: ", values[3])
        print(dict1)

    else:
        print("Invalid Account Number \n")
    intro()
            
        
                
def Withdrawal():
    global Net_balance
    Acc_no = int(input("Account Number: \n"))
    Withdrawal_amt =int(input("Withdrawal Amount \n"))
    values = dict1[Acc_no]
    Net_balance = values[3] - Withdrawal_amt
    print("Withdrawal Successful. Net balance is ", Net_balance)
    intro()
    
def Barchart():
    x = 10
    y = 20
    plt.bar(x, Amount_deposit)
    plt.bar(y,Net_balance)
    plt.show()
    intro()
    
    
def Exit():
    print("Thank you ! visit our branch again")
    sys.exit(0)
    
    
 
def intro():
    print("\t\t\t\t*********************")
    print("\t\t\t\t  aXess Digital Bank ")
    print("\t\t\t\t*********************")
    print("\t MAIN MENU")
    print("\t 1. Create Account")
    print("\t 2. View Account Details")
    print("\t 3. Withdrawal")
    print("\t 4. Bar chart")
    print("\t 5. Exit")
    choice = input("Enter you choice  \n")
    if choice == '1':
        Create_Account()
    elif choice == '2':
        View_AccountDetails()
    elif choice == '3':
        Withdrawal()
    elif choice == '4':
        Barchart()
    elif choice == '5':
        Exit()
    else:
        Exit()
        
    
    
        
intro() 