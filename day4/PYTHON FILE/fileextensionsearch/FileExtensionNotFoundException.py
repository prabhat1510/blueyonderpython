# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 16:15:31 2024

@author: UD SYSTEMS
"""

class FileExtensionNotFoundException(Exception):
    def __init__(self, message):
        self.message = message