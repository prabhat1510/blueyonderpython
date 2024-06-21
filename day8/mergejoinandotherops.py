# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 11:45:48 2024

@author: UD SYSTEMS
"""
import pandas as pd

print("************************Merge, Join and Concatenation of the Data Frames********************************************")
#merge,join and concatenate the dataframes
#concatenate dataframes example
myDict1={'A': ['A0', 'A1', 'A2', 'A3'],
'B': ['B0', 'B1', 'B2', 'B3'],
 'C': ['C0', 'C1', 'C2', 'C3'],
 'D': ['D0', 'D1', 'D2', 'D3']}
df1 = pd.DataFrame(myDict1, index=[0, 1, 2, 3])
myDict2={'A': ['A4', 'A5', 'A6', 'A7'],
 'B': ['B4', 'B5', 'B6', 'B7'],
 'C': ['C4', 'C5', 'C6', 'C7'],
 'D': ['D4', 'D5', 'D6', 'D7']}
df2 = pd.DataFrame(myDict2, index=[4, 5, 6, 7])
myDict3={'A': ['A8', 'A9', 'A10', 'A11'],
'B': ['B8', 'B9', 'B10', 'B11'],
'C': ['C8', 'C9', 'C10', 'C11'],
'D': ['D8', 'D9', 'D10', 'D11']}
df3 = pd.DataFrame(myDict3,index=[8, 9, 10, 11])


print(df1)
print(df2)
print(df3)

frames=[df1,df2,df3]
result=pd.concat(frames) #it returns new dataframe original dataframes remain entact
print("*************************")
print(result)
print(type(result))
print("*************************")
print(df1)
print("*************************")
print(df2)
print("*************************")
print(df3)


print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
# DataSet of number of sales made by an employee
sales = {'Tony': 103,
 'Sally': 202,
 'Randy': 380,
 'Ellen': 101,
 'Fred': 82
 }
# DataSet of all employees and the region they work in
region = {'Tony': 'West','Sally': 'South',
 'Carl': 'West',
 'Archie': 'North',
 'Randy': 'East',
 'Ellen': 'South',
 'Fred':'NaN',
 'Mo': 'East',
 'HanWei': 'NaN',
 }


#Make dataframes --  using from_dict function dataframe is created
sales_df=pd.DataFrame.from_dict(sales,orient="index",columns=["sales"])
region_df=pd.DataFrame.from_dict(region,orient="index",columns=["region"])

print(sales_df)
print(region_df)

#Using pd.DataFrame dataframe is created
sales_df1=pd.DataFrame([sales])
print(sales_df1)


print("*********************************Joining two dataframes******************")
joined_df=region_df.join(sales_df,how="left")
print(joined_df)


right_joined_df=region_df.join(sales_df,how="right")
print(right_joined_df)
print("######################################")
inner_joined_df=region_df.join(sales_df,how="inner")
print(inner_joined_df)

outer_joined_df=region_df.join(sales_df,how="outer")
print(outer_joined_df)
print("******************************************")
right_joined_df=sales_df.join(region_df,how="right")
print(right_joined_df)


print('****************************************Merge*************************************')
print(region_df)
print(sales_df)
merge_df=region_df.merge(sales_df,how='left',left_index=True,right_index=True)
print(merge_df)
print(merge_df.index)  
print(list(merge_df.index))
