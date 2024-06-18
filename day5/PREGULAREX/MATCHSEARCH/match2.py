# regular expression
import re
str = "India is our country. India is our Nation"


#search for the word nation
result = re.match( r'india', str, re.M|re.I)
if result:
         print("value found")
else:
         print("Not found")



#re.M - for multiple line in the string
#re.I - Ignorecase 
