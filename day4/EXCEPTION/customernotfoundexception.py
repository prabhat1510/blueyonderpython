# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 12:51:05 2024

@author: UD SYSTEMS
"""


#Custom exception class with CustomerNotFoundException
#Below class is inheriting the properties of Exception super class
class CustomerNotFoundException(Exception):
    def __init__(self, message):
        self.message = message
