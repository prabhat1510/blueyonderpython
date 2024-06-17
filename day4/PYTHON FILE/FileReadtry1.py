# Reading the Data From the File with Error handlig
fo=None

try:
    # Open a file
    fo = open("test.txt", "r")# If file doesn't exists it raise an exception
    str1=fo.read()
    print ("Read String is : ", str1)
#except Exception  
except FileNotFoundError as f:
    print(f)
    print("File is not found ")
 
finally:
    # Close the file
    print("bye from finally block")
    if fo != None:
        fo.close()
   

