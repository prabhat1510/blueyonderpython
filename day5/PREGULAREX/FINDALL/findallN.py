# findall function

import re

exampleString = '''
Jessica is 15 years old, and Daniel is 27 years old.12345
Edward is 97 years  2 old, and his Grandfather, Oscar, is 102.
'''

ages = re.findall(r'\d{1,3}',exampleString) # Returns all the numbers
names = re.findall(r'[A-Z][a-z]*',exampleString) # Returns the names starts with Capital Letter

print(ages)
print(names)
