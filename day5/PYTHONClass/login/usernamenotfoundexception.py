# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 14:17:10 2024

@author: UD SYSTEMS
"""

class UserNameNotFoundException(Exception):
    def __init__(self, message):
        self.message = message