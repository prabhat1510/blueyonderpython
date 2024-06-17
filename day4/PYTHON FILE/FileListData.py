# List Example

fo=open("outputtest.txt","w")

# List creation
empList = [ 2001, 'Shivani',2005, 'Sanjay', 2007, 'Babu']
#str=str(empList)
fo.write(str(empList))
#fo.write(empList)

#print ("employee Details : \n", empList)
print("Data written")
fo.close()














###specific element from List
##print("2nd Position : ", empList[1])
##
###printing Range of element
##print("1st to 4th element : ", empList[0:4])
##
##
###printing from 2nd element to last element
##print("2nd to last element : ", empList[1:])
##      
###printing the list two times
##print(empList*2)
