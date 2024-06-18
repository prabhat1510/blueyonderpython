# regular expression sub
import re
str="Avenue Road. Right Road Leads To Success"

s=re.sub("Road$", 'Rd',str)
print(s)

#search from the beginning
s=re.sub("^Road", 'Rd',str)
print(s)

#search from all the direction
s=re.sub(r'Road', 'Rd',str)
print(s)
