# regular expression  - findall function with file
import re
patt="^[AD]\w+"

try:
   # Open a file
    fo = open("demo1.txt",'r')
 
    for line in fo:
       if re.findall(patt,line):
           print(line)
    
     # Close the file
    fo.close()

except FileNotFoundError:
    print("File is not found")

