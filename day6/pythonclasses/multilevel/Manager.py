# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 12:37:38 2024

@author: UD SYSTEMS
"""

import Employee as e

class Manager(e.Employee):
    def __init__(self,empno,empname,dateofjoining,supervisor):
        e.Employee.__init__(self, empno,empname,dateofjoining)
        self.supervisior=supervisor
        
    
    