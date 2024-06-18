import re

programming = ["Python", "Java", "PHP", "C++"]

pat = "^B|^P|i$|H$"

for lang in programming:
    
    if re.search(pat,lang,re.IGNORECASE):
        print(lang , "FOUND")
    
    else:
        print (lang, "NOT FOUND")
