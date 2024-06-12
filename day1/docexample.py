# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 12:56:43 2024

@author: UD SYSTEMS
"""

def multiply(x,y):
    '''
    
        this function takes two numbers in the form of input and multiplies them.
        it displays the multiplication as the result.
    Parameters
    ----------
    x : Number.
    y : Number.

    Returns
    -------
    x*y

    '''
    return x*y


def show():
    '''
    This function displays a message.
    It shows a welcome message to the user.

    Returns
    -------
    None.

    '''
    print("Welcome to Python Tutorials")
#functions calling
result = multiply(10, 15)
print(result)
show()
print(show.__doc__)
print(multiply.__doc__)
print("**********************************************")
print(str.__doc__)
print("**********************************************")
print(str.__name__)
print("**********************************************")
print(show.__name__)