# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 09:46:38 2024

@author: UD SYSTEMS
"""

import pandas as pd

file = pd.read_csv("D:\\blueyonderpythons\\day8\\pandas_exercise\\emp1.csv")
print(file)
print(file.head(6))
print(file.tail(5))
print(file.columns)

print("****************4.  Display the columns: First Name, Gender, Team****************************")
print(file[["First Name", "Gender", "Team"]])
print("**************Below lines will column name******************************")
col_values = file.columns.values
print(col_values[0], col_values[1], col_values[7])

print("***********4.  Display the columns: First Name, Gender, Team****************************")
print(file[[col_values[0], col_values[1], col_values[7]]])

print("************5.  Rename the columns: First Name as Name, Bonus % as Bonus***************")
file = file.rename(columns={"First Name" : "Name", "Bonus %":"Bonus"})
print(file)
print(file[['Bonus']])
print("*********6.  Reorder the columns as Name, Gender, Team, Salary**********")
print(file[["Name", "Gender", "Team", "Salary", "Bonus", "Start Date", "Last Login Time", "Senior Management" ]])

print("**********7.  Add a column BonusAmt = (Bonus * Salary)/100************************")
file["BonusAmt"] = (file["Bonus"] * file["Salary"])/100
print(file)
print("*****************8.  Display the male records from the Product team****************************")
print(file[(file['Gender']=='Male') & (file['Team']=='Product')])
print("***********************9.  Display the Name and Team of the female members***********************")
df = file[(file['Gender']=='Female')]
#print(df)
print(df[['Name','Team']])

print("***************10. Find the minimum bonus amount of the male team members and display it along with the team************************")
df = file[(file.Gender == 'Male')][['Name','BonusAmt']].min()
print(df)