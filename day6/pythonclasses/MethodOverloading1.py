# method overloading in python

# overloaded function
def add(instanceOf, *args):
   
 if instanceOf == 'int':
          result = 0
 if instanceOf == 'str':
          result = '' 
       
 for i in args:
         result = result + i
 print(result) 	 
   

print("Python Method Overloading Example")
print (add('int', 3,4,5))
print (add('str', 'I',' am',' in', ' Python'))

