# searching for the word in a file
import re

try:
   # Open a file
    fo = open("demo1.txt",'r')

 
    for line in fo:
       if re.search(r"[s]\w+", line):
           print(line)
  

    
     # Close the file
    fo.close()

except Exception:
    print("File is not found")

