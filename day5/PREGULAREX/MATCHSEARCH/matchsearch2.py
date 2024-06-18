#Search v/s match function

import re

#match will search only in the beginning of the String
print("match function")
flag=re.match("c", "abcdef")
if flag:
    print("Found")
else:
    print("Not Found")


#search will search anywhere in the String
print("Search function")
flag=re.search("c", "abcdef")
if flag:
    print("Found")
else:
    print("Not Found")