# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 12:01:57 2024

@author: UD SYSTEMS
"""

import json

person = '{"name": "Bob", "languages": ["English", "French"]}'
person_dict = json.loads(person)

# Output: {'name': 'Bob', 'languages': ['English', 'French']}
print( person_dict)


# Output: ['English', 'French']
print(person_dict['languages'])

#Reading a json file
with open('D:\\blueyonderpythons\\day9\\person.json', 'r') as f:
  data = json.load(f)

# Output: {'name': 'Bob', 'languages': ['English', 'French']}
print(data)
print(type(data))
print(data["address"])
print(data["address"][0]["home"])
print(data["address"][0]["office"])


#Convert dict to JSON
person_dict = {'name': 'Bob',
'age': 12,
'children': None
}
person_json = json.dumps(person_dict)
print("******************************************")
# Output: {"name": "Bob", "age": 12, "children": null}
print(person_json)
print("******************************************")

'''
Here's a table showing Python objects and their equivalent conversion to JSON.

Python  	  JSON Equivalent
dict	       object
list, tuple	   array
str	           string
int,float,int  number
True	true
False	false
None	null
'''
 #Writing JSON to a file
person_dict = {"name": "Bob",
"languages": ["English", "French"],
"married": True,
"age": 32
}

with open('person.txt', 'w') as json_file:
  json.dump(person_dict, json_file)

# Python pretty print JSON
person_string = '{"name": "Bob", "languages": "English", "numbers": [2, 1.6, null]}'

# Getting dictionary
person_dict = json.loads(person_string)


# Pretty Printing JSON string back
print(json.dumps(person_dict, indent = 4, sort_keys=True)) 
#In the above program, we have used 4 spaces for indentation. And, the keys are sorted in ascending order.
#By the way, the default value of indent is None. And, the default value of sort_keys is False.
