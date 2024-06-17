# Reading the Data word by word from a file using for loop 

# Open a file
try:   
    fo = open("test.txt",'r',encoding = 'utf-8')

    # reading line by line
    for line in fo:
        for word in line.split():
            print(word)
   
     # Close the file
    fo.close()

except Exception:
    print("File is not found")
