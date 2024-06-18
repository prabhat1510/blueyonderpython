import re

str = 'cat an example word:cat'

pat = "cat$"  # checks for the word at the end

m1 = re.search(pat, str)

# If-statement after search() tests if it succeeded
if m1:                      
    print('found', m1.group()) ## 'found word:cat'
else:
    print('did not find')
