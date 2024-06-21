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