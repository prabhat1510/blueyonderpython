# checks for the number entry


import re

empno = re.compile(r"[^0-9]")

eno = input ("Please, enter employee No: ")

while empno.search(eno):
    print ("Please enter your empno correctly!")
    eno = input ("Please, enter employee No: ")
else:
         print("Employee No : ", eno)
