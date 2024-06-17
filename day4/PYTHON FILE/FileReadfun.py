



# Reading the Data From the File

# Open a file
fo = open("test.txt", "r")

# Reading the data from a file
str1 = fo.read(10);
print ("Read String is : ", str1)

str=fo.read()
print ("Read String is : ", str1)

# Close opend file
fo.close()
