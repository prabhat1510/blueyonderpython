# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 10:08:40 2024

@author: UD SYSTEMS
"""

import pandas as pd

print("**************************************")
mdict={"country":["Brazil","Russia","India","China","South Africa"],
       "capital":["Brasialia","Muscow","New Delhi","Beijing","Pretoria"],
       "area":[8.516,17.10,3.286,9.597,1.221],
       "population":[200.4,143.5,1252,1357,52.98]}

brics=pd.DataFrame(mdict)
#print(brics)

#In o/p Pandas has assigned a key for each country as 
#the numerical values 0 through 4
print(brics)
print(type(brics))
#After creating dataframe we can assign index as below
brics.index=["BR","RU","IN","CH","SA"]
print(brics)

#It will give us the column values in the form 
colHeader= brics.columns.values
print(colHeader)
print(type(colHeader))

print(colHeader[0])
colHeader[0]='Region'
print(colHeader[0])
print(colHeader)
print(brics)

print("*********************************************")
brics.set_index("country",inplace=True)
print(brics)

print("************************************************")
print(brics["area"]) #getting particular column data
print(brics["area"].mean())#mean of all data present in particular 
print(round(brics["area"].mean(),2))

print(brics.describe())

"""
    Using data using loc and iloc
    loc:- is a label-based which means that you have to specify rows and columns based on their row and column labels.
    iloc:- is integer index based, so we have to specify rows and columns by their integer index like we did it the below example
"""
print(brics)
print(brics.iloc[2])
print(brics.loc['China'])


brics.to_csv("D:\\blueyonderpythons\\day8\\brics.csv")
brics.to_json("D:\\blueyonderpythons\\day8\\brics.json")
brics.to_excel("D:\\blueyonderpythons\\day8\\brics.xlsx")