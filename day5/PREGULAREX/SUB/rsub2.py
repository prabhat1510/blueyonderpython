# regular expression



import re
str="India is our nation"
print(str)

#change nation to country
# $ means at the end of the sentence
print(re.sub('nation$','country',str))
      

