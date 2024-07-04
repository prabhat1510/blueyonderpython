# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 12:10:25 2024

@author: UD SYSTEMS
"""

from flask import Flask
from flask_restful import Api, Resource
from resources import EmployeeListResource,EmployeeResource

app = Flask(__name__)
api = Api(app)

api.add_resource(EmployeeListResource,'/employees')    
api.add_resource(EmployeeResource,'/employees/<int:emp_id>')


if __name__ == '__main__':
    app.run(debug=True)