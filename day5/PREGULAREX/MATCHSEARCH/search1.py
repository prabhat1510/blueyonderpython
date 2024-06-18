# RegularExpression search function



import re

#Searches anywhere in the  of the String
result=re.search(r'India', 'India is our nation India')
print(result)
if result:
         print("Word Found : ", result.group(0))
         
         
else:
         print("Not Found",result)



#search syntax
# re.search(pattern,string)
#Search for the word in the String based on the given pattern any where in the String


#group() method Helps to return the match string returns None if the match is not found
