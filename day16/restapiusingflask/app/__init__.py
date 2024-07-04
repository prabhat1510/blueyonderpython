# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 09:42:14 2024

@author: UD SYSTEMS
"""

from flask import Flask
app=Flask(__name__)
from app import routes

'''

    By default Flask will return HTML response
    It internally uses Jinja for rendering HTML templates
'''