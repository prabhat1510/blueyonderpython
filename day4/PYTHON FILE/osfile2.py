# Example 

import os

fd = "demo.txt"
 
file = os.popen(fd, 'w')
file.write("Hello")  # writing data to the file


file = os.popen(fd, 'r')
text = file.read()
print(text)




