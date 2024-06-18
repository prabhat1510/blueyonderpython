# regular expression  - findall function



import re
text = "India is our nation. India is our Motherland"
print(text)

#search for the word nation
result = re.findall('nation',text)
print(result)


result = re.findall('India',text)
print(result)

result = re.findall('is',text)
print(result)

result = re.findall('our',text)
print(result)

#findall(<search word>,<string>)



