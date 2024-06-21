# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 12:05:46 2024

@author: UD SYSTEMS
"""

print('***************Comparing two datasets from different dataframe**************************')  
import numpy as np
import pandas as pd 

firstProductSet = {'Product1': ['Computer','Phone','Printer','Desk'],
                   'Price1': [1200,800,200,350]
                   }
df1 = pd.DataFrame(firstProductSet,columns= ['Product1', 'Price1'])
print(df1)

secondProductSet = {'Product2': ['Computer','Phone','Printer','Desk'],
                    'Price2': [900,800,300,350]
                    }
df2 = pd.DataFrame(secondProductSet,columns= ['Product2', 'Price2'])
print (df2)

df1['Price2'] = df2['Price2'] #add the Price2 column from df2 to df1
print(df1)
df1['pricesMatch?'] = np.where(df1['Price1'] == df1['Price2'], 'True', 'False')  #create new column in df1 to check if prices match
print (df1)

print(df1['Price1'][0])


print('*******************************another example of merge***********************')
df1 = pd.DataFrame({'lkey': ['foo', 'bar', 'baz', 'foo'],
                    'value': [1, 2, 3, 5]})
df2 = pd.DataFrame({'rkey': ['foo', 'bar', 'baz', 'foo'],
                    'value': [5, 6, 7, 8]})
print(df1)
print(df2)
#Merge df1 and df2 on the lkey and rkey columns. The value columns have the default suffixes, _x and _y, appended.
mergedf1=df1.merge(df2, left_on='lkey', right_on='rkey')
print(mergedf1)

#Merge DataFrames df1 and df2 with specified left and right suffixes appended to any overlapping columns.
mdf1=df1.merge(df2, left_on='lkey', right_on='rkey',
          suffixes=('_left', '_right'))
print(mdf1)

#Merge DataFrames df1 and df2, but raise an exception if the DataFrames have any overlapping columns.
#ValueError: columns overlap but no suffix specified: Index(['value'], dtype='object')
#print(df1.merge(df2, left_on='lkey', right_on='rkey', suffixes=(False, False)))

print('*************************group by function example on sales and region dataframe*******************')
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

merge_df=region_df.merge(sales_df,how='left',left_index=True,right_index=True)
print(merge_df)
print(merge_df.index)  
print(list(merge_df.index))

print(merge_df)

group_df=merge_df.groupby(by='region').sum()
print(group_df)

#print(group_df.reset_index(inplace=False)) #Set index of the data frame and returns the object after operation when inplace = False
#Set index of the data frame and it returns nothing
group_df.reset_index(inplace=True)
print(group_df)


employee_contrib=merge_df.merge(group_df,how='left',left_on='region',right_on='region',suffixes=('','_region'))
print(employee_contrib)
employee_contrib=employee_contrib.set_index(merge_df.index)
print(employee_contrib)


#Data munging
employee_contrib.to_json("D:\\blueyonderpythons\\day8\\employee_contrib.json")
employee_contrib.to_html("D:\\blueyonderpythons\\day8\\employee_contrib.html")
employee_contrib.to_excel("D:\\blueyonderpythons\\day8\\employee_contrib.xlsx")
employee_contrib.to_csv("D:\\blueyonderpythons\\day8\\employee_contrib.csv")
