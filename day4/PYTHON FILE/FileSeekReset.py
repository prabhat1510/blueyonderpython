# Changing the file pointer position and reading the data.



# Open a file
try:
   
    fo = open("test.txt", "r")
    str1=fo.read(10)
    print ("Reads First 10 Characters ", str1)
    print("Current position ", fo.tell()) #Current position cursor

    fo.seek(0) # bring the file cursor to initial position

    strr=fo.read()
    print("full file contents : ", strr)
    
     # Close the file
    fo.close()

except Exception:
    print("File is not found")
finally:
    print("bye from finally block")

