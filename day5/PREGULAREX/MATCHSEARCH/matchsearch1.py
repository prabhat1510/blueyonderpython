# regular expression match v/s search
import re
str1 = "India is our nation";

#match will search for the word only in the beginning of the string
result = re.match( r'nation', str1)
print("Output of the match function :")
if result:
         print("value found")
else:
         print("Not found")


#search will search for the word anywhere in the string
result = re.search( r'nation', str1)
print("Output of the search function :")
if result:
         print("value found")
else:
         print("Not found")
