# importing the pickle package
import pickle   


pk = open("Emp.pickle","rb") # opening the file

emp = pickle.load(pk) #reading the data

print(emp) #printing the output
