# Phone number pattern search

import re

phonePattern = re.compile(r'^(\d{3})-(\d{3})-(\d{4})$')
pp=phonePattern.search('800-587-1212').groups()          
print(pp)



#Note: Read the regular expression from left to write
#\d check for digits
#{3} checks for exact 3 digits
