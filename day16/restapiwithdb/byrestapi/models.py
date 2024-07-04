# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 12:10:25 2024

@author: UD SYSTEMS
"""

#from flask import Flask, request,current_app
#from flask_sqlalchemy import SQLAlchemy
#from flask_marshmallow import Marshmallow
from app import db
#from dbconfig import db

#Define data model
class Employee(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    ename=db.Column(db.String(50))
    def __repr__(self):
        return '<Employee %s>' % self.ename
    