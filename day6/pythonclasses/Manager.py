# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 12:27:59 2024

@author: UD SYSTEMS
"""
import Employee as e

class Manager(e.Employee):
    def __init__(self,empno,empname,dateofjoining,dept,supervisor):
        e.Employee.__init__(self, empno,empname,dateofjoining,dept)
        self.supervisior=supervisor
        
    def show(self):
        print("Emp no : ", self._empno)
        print("Emp Name :", self._empname)
    
    
# object creation

objS=Manager(10,'Raj','11-11-2000','IT','Yes')
objS.show()
