# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 12:18:03 2024

@author: UD SYSTEMS
"""

# importing the base class from a module

import inherit1 as cs1


class SBAcct(cs1.Account):
    def __init__(self, accno,bal):
        cs1.Account.__init__(self, accno)
        self.bal=bal
        
    def show(self):
        print("Account no : ", self._accno)
        print("Balance :", self.bal)
    
    
# object creation

objS=SBAcct(10,2000.00)
objS.show()
