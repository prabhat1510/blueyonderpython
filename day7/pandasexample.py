# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 15:50:03 2024

@author: UD SYSTEMS
"""

import pandas as pd
#pip install pandas

dictOne={ "HPI":[80,90,70,60],"Int_Rate":[2,1,2,3],"IND_GDP":[50,45,45,67]}
df1 = pd.DataFrame(dictOne)
print(df1)
df1= pd.DataFrame(dictOne, index=[2001, 2002,2003,2004])
print(df1)
df2=pd.DataFrame({ "HPI":[81,90,70,60],"Int_Rate":[2,1,2,3],"IND_GDP":[50,45,45,67]}, index=[2005, 2006,2007,2008])
df3=pd.DataFrame({ "HPI":[80,95,75,60],"Int_Rate":[2,1,2,3],"IND_GDP":[50,45,45,67]}, index=[2005, 2006,2007,2008])
print(df2)
print(df3)

print("***********************************************")
dfMerge=pd.merge(df1,df2)
print(dfMerge)

dfMerge2=pd.merge(df1,df3)
print(dfMerge2)
print("**************Left Join***********")
print(df1)
print(df2)
dfMerge=pd.merge(df1,df2,how="left")
print(dfMerge)
#dfMerge2=pd.merge(df1,df3,how="left")
#print(dfMerge2)

print("*********Right Join**************")
dfMerge=pd.merge(df1,df2,how="right")
print(dfMerge)
#dfMerge2=pd.merge(df1,df3,how="right")
#print(dfMerge2)

print("*********Outer Join**************")
print(df1)
print(df2)
print(df3)
dfMerge1=pd.merge(df1,df2,how="outer")
print(dfMerge1)
dfMerge3=pd.merge(df1,df3,how="outer")
print(dfMerge3)
print("******************Cross Join********************")
dfMerge4=pd.merge(df1,df3,how="cross")
print(dfMerge4)
print("*********Another Left Index *************")
dfMerge1=pd.merge(df1,df2,left_index=True,right_index=True)
print(df1)
print(df2)
print(df3)
print(dfMerge1)
dfMerge3=pd.merge(df2,df3,left_index=True,right_index=True)
print(dfMerge3)

print("*********Left_On and Right_On******")
df4 = pd.DataFrame({'lkey': ['foo', 'bar', 'baz', 'foo','bar'],'value': [1, 2, 3, 5,6]})
df5 = pd.DataFrame({'rkey': ['foo', 'bar', 'baz', 'foo'],'value': [5, 6, 7, 8]})
#df4.merge(df5, left_on='lkey', right_on='rkey', suffixes=(False, False))
df4.merge(df5,left_on='lkey', right_on='rkey',suffixes=('_left', '_right'))
print(df4)

df5.merge(df4,left_on='rkey', right_on='lkey',suffixes=('_left', '_right'))
print(df5)