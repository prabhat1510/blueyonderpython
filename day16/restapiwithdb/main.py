# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 12:10:25 2024

@author: UD SYSTEMS
"""

from flask import Flask, request,current_app
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api, Resource

'''
def create_app():
    app =Flask(__name__)
    with app.app_context():
        #init_db()
        current_app.config["ENV"]
    return app
#app = Flask(__name__)
app=create_app()
'''
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@localhost:3306/flasktestdb'

db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)

#Define data model
class Employee(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    ename=db.Column(db.String(50))
    def __repr__(self):
        return '<Employee %s>' % self.ename
    
class EmployeeSchema(ma.Schema):
    class Meta:
        model = Employee
        fields = ("id","ename")

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
    
api.add_resource(EmployeeListResource,'/employees')    
api.add_resource(EmployeeResource, '/employees/<int:emp_id>')


if __name__ == '__main__':
    app.run(debug=True)