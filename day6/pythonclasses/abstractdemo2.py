# abstract class in Python
# implement the Abstract base class by using abc
#standard library module in Python 3.4
#https://www.smartfile.com/blog/abstract-classes-in-python/

#Importing abc module
from abc import ABC, abstractmethod

#Abstract Base class
class mathAbcClass(ABC):
         #paramaterized constructor
         def __init__(self,num1, num2):
                  self.num1=num1
                  self.num2=num2
                  

         # Abstract method
         @abstractmethod
         def execute(self):
                  pass

# Derived class
class addNum(mathAbcClass):
         pass
         

         #paramaterized constructor
         def __init__(self,num1, num2):
                  mathAbcClass.__init__(self,num1, num2)

         #Implementing the abstrat method
         def execute(self):
                   s=self.num1+self.num2
                   print("Sum = ", s)


#create the object of the base class
obj1=mathAbcClass(2,4)  # can't create the object for the abstract class

#create the object for the derived class
##objA1=addNum(10,30)
##objA1.execute()#calling the execute method


#By default the python will not force the derived classes to implement the Abstract base class method
#ABC is a class in abc module used to create the Abstract class in Python
#@abstractmethod - decorator used to create the abstract class
# https://docs.python.org/3/library/abc.html for more details on the abstract class


