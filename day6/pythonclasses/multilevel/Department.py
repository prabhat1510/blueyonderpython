# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 12:38:23 2024

@author: UD SYSTEMS
"""
import Manager as m
class Department(m.Manager):
       def __init__(self,empno,empname,dateofjoining,supervisor,dept):
            m.Manager.__init__(self, empno,empname,dateofjoining,supervisor)
            self.dept=dept
            
       def show(self):
            print("Emp no : ", self._empno)
            print("Emp Name :", self._empname)
            print("Date Of Joining: ", self._dateofjoining)
            #print("Supervisior :", self.supervisor)
            #print("Dep :", self.dept)
            
            
