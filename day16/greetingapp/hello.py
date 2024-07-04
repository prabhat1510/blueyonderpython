# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 10:18:10 2024

@author: UD SYSTEMS
"""


from flask import Flask # First we imported the Flask class. An instance of this class will be our WSGI application

app = Flask(__name__) # Created an instance of Flask class.The 1st argument is the name of the application's module or package.
#__name__ is a convenient short cut for this.

#We then use the route() decorator to tell Flask what URL should trigger our function

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"