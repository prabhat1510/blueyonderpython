# Ex re.compile() function - checks whether the name contains only letters


import re

name_check = re.compile(r"[^A-Za-zs.]")

name = input ("Please, enter your name: ")

while name_check.search(name):
    print ("Please enter your name correctly!")
    name = input("Please, enter your name: ")

else:
         print("Name Entered is : ", name)






#re.compile() function we can compile pattern into pattern objects, 
#which have methods for various operations such as searching for pattern matches
#or performing string substitutions. 
