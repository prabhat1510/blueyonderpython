# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 12:10:25 2024

@author: UD SYSTEMS
"""


from flask_marshmallow import Marshmallow
from dbconfig import db
from serializers import EmployeeSchema
from models import Employee

employee_schema=EmployeeSchema()
employees_schema=EmployeeSchema(many=True)

#Restful Routes
class EmployeeListResource(Resource):
    def get(self):
        emps=Employee.query.all()
        return employees_schema.dump(emps)
    
    def post(self):
        new_emp = Employee(
            ename=request.json['ename']
            )
        db.session.add(new_emp)
        db.session.commit()
        return employee_schema.dump(new_emp)
    
class EmployeeResource(Resource):
    def get(self, emp_id):
        emp = Employee.query.get_or_404(emp_id)
        return employee_schema.dump(emp)

    def patch(self, emp_id):
        emp = Employee.query.get_or_404(emp_id)

        if 'ename' in request.json:
            emp.ename = request.json['ename']

        db.session.commit()
        return employee_schema.dump(emp)

    def delete(self, emp_id):
        emp = Employee.query.get_or_404(emp_id)
        db.session.delete(emp)
        db.session.commit()
        return '', 204
    
