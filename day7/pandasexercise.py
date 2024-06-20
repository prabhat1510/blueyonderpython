# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 16:46:11 2024

@author: UD SYSTEMS
"""
import pandas as pd 

mtCars = pd.read_csv("D:\\blueyonderpythons\\day7\\frozensetpptandpandas\\mtcars.csv")
print(mtCars)
print(type(mtCars))

print(mtCars.head())
print(mtCars.tail())

print(mtCars.head(10))
print(mtCars.tail(6))
print('####################')
print(mtCars.columns)
print('####################')
print(mtCars.index)
print('####################')
print(mtCars.dtypes)
print('####################')
print(mtCars.values)

print('####################')
print(mtCars.shape)
print('####################')
print(mtCars.size)