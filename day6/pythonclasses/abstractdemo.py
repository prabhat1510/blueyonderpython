#Exmple - Abstrat class in python
from abc import abstractmethod



class Shape:        # Abstract base class
   # non abstract method
   def demo(self):
      print("Welcome to Abstract class");

   @abstractmethod
   def draw(self):   # abstract method
      #raise NotImplementedError("Subclass must implement abstract method")
      pass

class Rectangle(Shape): # Derived class
     def draw(self):# abstract method implementation
         print ('Drawing Rectangles')

  
 

class Circle(Shape): # Derived class
   def draw(self):  # abstract method implementation
      print ('Drawing Circles')

print('Python Abstract class\n')
# Creating the object of Rectangle class

objRect=Rectangle()
print("Rectangle class : ")
objRect.demo()
objRect.draw()

# Creating the object of Circle class`
objCir=Circle()
print("\n\nCircle class : ")
objCir.demo()
objCir.draw()

# Python 3 abc module represents the abstract from std library
# @abstractmethod enforces the derived class to implement the abstract method
