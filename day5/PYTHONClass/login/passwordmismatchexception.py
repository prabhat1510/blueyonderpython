# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 14:18:32 2024

@author: UD SYSTEMS
"""

class PasswordMismatchException(Exception):
    def __init__(self, message):
        self.message = message