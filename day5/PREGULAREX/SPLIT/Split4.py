import re

str1="Hello My\\Name\\ is\\ Sanjay"

str2=re.split("\\\\",str1)

#str2=re.split(r"\\",str1)

for i in str2:
    print(i)

# In this expression delimiting charater willbe \\ where it has a specifal meaning in python
# "\\\\" before each slash we need to provide another slash
# r if you use it will cancel the special meaning of \\ in the expression
