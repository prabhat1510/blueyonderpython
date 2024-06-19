# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 12:51:28 2024

@author: UD SYSTEMS
"""

class Base:
    # Constructor to set Data
    def __init__(self, name, roll, role):
        self.name = name
        self.roll = roll
        self.role = role
 
# Intermediate Class: Inherits the Base Class
class Intermediate(Base):
    # Constructor to set age
    def __init__(self, age, name, roll, role):
        super().__init__(name, roll, role)
        self.age = age
 
# Derived Class: Inherits the Intermediate Class
class Derived(Intermediate):
    # Method to Print Data
    def __init__(self, age, name, roll, role,dob):
        super().__init__(age, name, roll, role)
        #self.__dob_=dob
        self.dob=dob
 
    def Print_Data(self):
        print(f"The Name is : {self.name}")
        print(f"The Age is : {self.age}")
        print(f"The role is : {self.role}")
        print(f"The Roll is : {self.roll}")
        print(self.dob)
# Creating Object of Base Class
obj = Derived(21, "Lokesh Singh", 25, "Software Trainer",'11-11-2020')
 
# Printing the data with the help of derived class
obj.Print_Data()