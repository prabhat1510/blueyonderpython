# Reading the Data line by line using for loop 


# Open a file
try:   
    fo = open("test1.txt",'r')

    # reading line by line
    for line in fo:
         print(line)
   
     # Close the file
    fo.close()

except Exception:
    print("File is not found")
