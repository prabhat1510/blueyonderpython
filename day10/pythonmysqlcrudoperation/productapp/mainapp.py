# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 16:29:57 2024

@author: UD SYSTEMS
"""
import sys
import userregistration


def main():
    
    while(True):
        print("***************Welcome to Product App******************")
        print("***************Select from below options***************")
        print("***************1. To Register Yourself enter 1 ********")
        print("***************2. To Login enter 2*********************")
        print("***************3. To Exit enter 3**********************")
        choice = input("Enter your option ")
        if(choice != "" and choice in ('1','2','3')):
            if(int(choice) == 1):
                userregistration.registerUser()
                #pass
            elif(int(choice) == 2):
                userregistration.login()
                #pass
            else:
                sys.exit(0)
        else:
            print("Enter appropriate options")



if __name__ == "__main__":
    main()