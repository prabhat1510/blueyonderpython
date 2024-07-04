# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 09:42:14 2024

@author: UD SYSTEMS
"""

from app import app
from markupsafe import escape
@app.route("/index")
def index():
    return 'Hello World !!!'

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

'''
        Converter types is optional
         string  (default) accepts any text without a slash 
         int accepts +ve integers
         float   accepts +ve floating point values
         path  like string but also accepts slashes
         uuid  accepts UUID strings
'''

'''

    By default Flask will return HTML response
    It internally uses Jinja for rendering HTML templates
'''

@app.route("/user/<username>")
def show_user_profile(username):
    return f'User {escape(username)}'

@app.route("/post/<int:post_id>")
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'