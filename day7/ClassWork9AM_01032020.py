# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 10:05:11 2020

@author: Admin
"""

vowels=("a","e","i","o","u","o")
fset1=frozenset(vowels)
print("Frozen set is:",fset1)
print(type(fset1))
print("Empty Frozen set is:",frozenset())

person={"name": "John", "age": 23, "sex": "male"}
fSet2 = frozenset(person)
print('The frozen set is:', fSet2)

print(person.keys())
print(fset1 & fSet2) #Intersection
print(fset1 | fSet2)


#Example of Pandas Slicing
import pandas as pd
#pandas.DataFrame()
XYZ_web= {'Day':[1,2,3,4,5,6], "Visitors":[1000, 700,6000,1000,400,350], "Bounce_Rate":[20,20, 23,15,10,34]}
print(XYZ_web)
df= pd.DataFrame(XYZ_web)
print(df)

#df.set_index("Day",inplace=True)
#print(df)
#df.set_index("Visitors",inplace=True)
#print(df)
print("**************")
print(df.tail(2))
print("***************")
print(df.head(4))

mtCarsData=pd.read_csv("C:\\Users\\Admin\\Documents\\Python Scripts\\mtcars.csv")
#print(mtCarsData)
dfCars=pd.DataFrame(mtCarsData)
print(dfCars)
print(dfCars.head())
dfCars=dfCars.rename(columns={"Unnamed: 0":"Model"})
print(dfCars)

titanicData=pd.read_csv("C:\\Users\\Admin\\Downloads\\titanic\\train.csv")
tDf=pd.DataFrame(titanicData)
print(tDf.head(10))
print(tDf[:3])
print(tDf[::-1])
print(tDf[50:54])
import numpy as np
myList=[1,3,5,np.nan,6,8]
s=pd.Series(myList)
print(s)
coList=tDf["PassengerId"]
print(coList)
print(type(coList))

#xList=tDf[:1]
#From Original DataFrame take one record it will give you a DataFrame
xList=tDf[:1]
print(xList) #Dataframe we get
print(type(xList)) # Type of Dataframe
#listFromDf=list(xList)
listFromDf=xList.values.tolist() #Convert Dataframe values to list
print(listFromDf)

conertDfToS=pd.Series(listFromDf) #Creating series from Dataframe values
print(conertDfToS)

