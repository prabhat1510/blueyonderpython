
import re



str = 'an example word:cat!!'
found = re.search(r'word:\w\w\w', str)
# If-statement after search() tests if it succeeded
if found:                      
   print ('found', found.group()) ## 'found word:cat'
else:
   print ('did not find')
