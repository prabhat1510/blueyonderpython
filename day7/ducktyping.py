# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 09:30:06 2024

@author: UD SYSTEMS
"""

class Duck:
    def swim(self):
        print("The duck is swimming")

    def fly(self):
        print("The duck is flying")

class Swan:
    def swim(self):
        print("The swan is swimming")

    def fly(self):
        print("The swan is flying")

class Albatross:
    def swim(self):
        print("The albatross is swimming")

    def fly(self):
        print("The albatross is flying")
        
'''        
birds = [Duck(), Swan(), Albatross()]

for bird in birds:
     bird.fly()
     bird.swim()
'''
duck = Duck()
swan = Swan()
alba = Albatross()

duck.fly()
duck.swim()
swan.fly()
swan.swim()
alba.fly()
alba.swim()