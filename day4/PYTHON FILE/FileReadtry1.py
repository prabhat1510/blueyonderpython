# Reading the Data From the File with Error handlig
fo=None

try:
    # Open a file
    fo = open("test.txt", "r")
    str1=fo.read()
    print ("Read String is : ", str1)
  
except Exception:
    print("File is not found")

finally:
    # Close the file
    print("bye from finally block")
    if fo != None:
        fo.close()
   

