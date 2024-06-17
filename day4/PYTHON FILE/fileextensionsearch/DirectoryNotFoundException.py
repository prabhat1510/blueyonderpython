# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 16:13:52 2024

@author: UD SYSTEMS
"""

class DirectoryNotFoundException(Exception):
    def __init__(self, message):
        self.message = message