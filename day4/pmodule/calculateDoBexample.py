# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 10:26:05 2024

@author: UD SYSTEMS
"""


import datetime


def calculateAge(date1):
     
    todaysDate = datetime.date.today()
    age = todaysDate-date1
    return age

#User input
dayOfBirth= int(input('Enter day of birth'))
monthOfBirth= int(input('Enter month of birth'))
yearOfBirth= int(input('Enter year of birth'))

#Formatting -convert dob to datetime object
dob=datetime.date(yearOfBirth,monthOfBirth,dayOfBirth)

print(calculateAge(dob))




# Get the current date
now = datetime.datetime.now()

# Ask the user for their date of birth
print("Enter your date of birth (YYYY-MM-DD):")
dob_input = input()

# Parse the user's input into a datetime object
birthday = datetime.datetime.strptime(dob_input, "%Y-%m-%d")

# Calculate the difference between the current date and the birthday
difference = now - birthday

# Calculate the person's age in years
age_in_years = difference.days // 365

print(f"You are {age_in_years} years old.")