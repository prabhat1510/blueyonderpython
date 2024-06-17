# Reading the Data line by line using readline function
# Open a file
try:
   
    fo = open("test1.txt",'r')

    # reading line by line
    print(fo.readline()) # Reads the single line

    # reading line by line
    print(fo.readlines()) # Reads multiple lines
    
     # Close the file
    fo.close()

except Exception:
    print("File is not found")
