# RegularExpression match function
import re


#Searches anywhere in the String
result=re.match(r'India', 'India is our nation')
if result:
         print("Word Found : ", result.group(0))
else:
         print(result)


#Searches only in the beginning of the String
result=re.match(r'^India', 'India is our nation')
if result:
         print("Word Found : ", result.group(0))
else:
         print(result)


#Searches at the End of the String
result=re.match(r'India$', 'India is our nation')
if result:
         print("Found : ", result.group(0))
else:
         print("Not Found",result)



#match syntax
# re.match(pattern,string)

#Search for the word in the String based on the given pattern

#group() method Helps to return the match string returns None if the match is not found




