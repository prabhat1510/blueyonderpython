import re

#Searches anywhere in the  of the String
result=re.finditer(r'India', 'India is our nation. India is a developing nation')
print(result)
i=0
for m in result:
         print(m)
         print(m.group(i))

#re.finditer it will return an Iterator Object and use it to iterate over all found matches.



