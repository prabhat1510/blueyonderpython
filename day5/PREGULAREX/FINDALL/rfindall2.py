##Python program that uses findall

import re

# Input.
value = "abc 123 def 456 dot map pat"

# Find all words starting with d or p.
list = re.findall("[dp]\w+", value)

# Print result.
print(list)


#Pattern: [dp]\w+
#[dp]     A lowercase d, or a lowercase p.
#\w+      One or more word characters.


#Another example
text = "India is our nation. India is our Motherland"
#result = re.findall(r'\bo\w*r\b', text)
result= re.findall(r"o\w*r\b", text)
print(result)

#Mobile number validation
#mobile ='9999106211'
mobile ='9699106211'
res = re.findall('^[6-9]\d{9}$', mobile)
print(res)