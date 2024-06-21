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

dfCars=mtCars.rename(columns={"Unnamed: 0":"Model"})
print(dfCars)
dfCars=dfCars.rename(columns={"mpg":"Mileage"})
print(dfCars)

print(dfCars.head(10))
print(dfCars[:3])
print("********************************************")
print(dfCars[::-1]) #Reverse the dataframe
print(dfCars[20:24])
print("********************************************")
#print(dfCars)

colHeader=dfCars.columns.values
print(colHeader)
colHeader[0]="Cars"
print(colHeader[0])
print(dfCars)
print(dfCars.columns.values)
dfCars.set_index("Mileage",inplace=True)

print(dfCars)