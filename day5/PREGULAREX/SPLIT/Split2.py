import re

str1=r"Hello My\tName is Sanjay"
print(str1)
str2=re.split("\W",str1)
print(str2)



#"\W" represents non-alphanumeric character
