# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 14:37:57 2024

@author: UD SYSTEMS
"""

class Employee:
    #constructor
    def __init__(self,empNo,empName):
        self.eNo=empNo
        self.eName=empName
        
    def getEmpNo(self):
        return self.eNo
    def getEmpName(self):
        return self.eName
    
'''
emp1 = Employee(1,'Charisma')
emp2 = Employee(2,'Champa')
emp3 = Employee(3,'Chandana')
emp4 = Employee(4,'Lakshmi')
emp5 = Employee(5,'Harshitha')
emp6 = Employee(6, 'Radhika')
listOfEmployee = [emp1,emp2,emp3,emp4,emp5,emp6]
'''
listOfEmployee=list()
try:
    while True:
        choice = input("Want to enter employee details Y/N: ")
        if choice == 'Y':
            empNo=int(input('Enter employee no : '))
            empName=input('Enter employee name : ')
            emp =Employee(empNo,empName)
            listOfEmployee.append(emp)
        else:
            break
        
except ValueError:
        print("Enter appropriate value")

for e in listOfEmployee:
    print(e.getEmpNo())
    print(e.getEmpName())
