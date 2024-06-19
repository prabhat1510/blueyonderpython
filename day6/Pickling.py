# importing the pickle package
import pickle   

#creating the dictionary
emp = {1:"A",2:"B",3:"C",4:"D",5:"E"}

#Opening the file to send the data
pk = open("Emp.pickle","wb")

pickle.dump(emp, pk) #storing the data

pk.close()# closing the file

print("Data is written")


#Pickle is used for serializing and de-serializing Python object structures, 
#also called marshalling or flattening.

#Serialization refers to the process of converting an object in memory 
#to a byte stream that can be stored on disk or sent over a network. 
#Deserialization - Restoring the information back to the python object.


##You can pickle objects with the following data types:
##Booleans,Integers,Floats,Complex numbers,(normal and Unicode) ##Strings,Tuples,Lists,Sets
