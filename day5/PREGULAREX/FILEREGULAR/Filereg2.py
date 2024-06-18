# Reading the Data line by line using readline function
import re

try:
   # Open a file
    fo = open("demo2.txt",'r')

  

 
    for line in fo:
       if re.search(r"[S]\w+", line):
           print(line)

##    for line in fo:
##       if re.search(r"^[S]\w+", line):
##           print(line)    

    
  

    
     # Close the file
    fo.close()

except Exception:
    print("File is not found")
