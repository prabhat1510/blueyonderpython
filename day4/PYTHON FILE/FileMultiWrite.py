# Writing the data into file in different lines



with open("test1.txt",'w') as f:

   f.write("my first file\n")
   f.write("This file\n\n")
   f.write("contains three lines\n")
   f.close()

print("Data is written to the file")






flName=input("Enter a filename ")
with open(flName,'w') as f: