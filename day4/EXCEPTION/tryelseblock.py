# Exception Handling with else block with try block



try:
   a=10/2
   print ("Output : ", a)

except ZeroDivisionError:
    print("No. Can't be divieded by Zero")
    
else:
    print("No Exception")

print("At the end of the program")