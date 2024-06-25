# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 16:29:57 2024

@author: UD SYSTEMS
"""
import sys
import userregistration


def main():
    print("***************Welcome to Product App******************")
    print("***************Select from below options***************")
    print("***************1. To Register Yourself enter 1 ********")
    print("***************2. To Login enter 2*********************")
    print("***************3. To Exit enter 3**********************")
    while(True):
        choice = int(input("Enter appropriate option "))
        if(choice == 1):
            userregistration.registerUser()
            #pass
        elif(choice == 2):
            userregistration.login()
            #pass
        else:
            sys.exit(0)
    



if __name__ == "__main__":
    main()