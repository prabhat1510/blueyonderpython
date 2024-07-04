# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 12:10:25 2024

@author: UD SYSTEMS
"""

from flask_marshmallow import Marshmallow
    
class EmployeeSchema(ma.Schema):
    class Meta:
        model = Employee
        fields = ("id","ename")

#employee_schema=EmployeeSchema()
#employees_schema=EmployeeSchema(many=True)

