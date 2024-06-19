#Exmple - Runtime polymorphism in python

class Shape:        # define parent class
   def draw(self):
      print ('Drawing various shapes')

class Rectangle(Shape): # define child class
   def draw(self):
      print ('Drawing Rectangles')

class Circle(Shape): # define child class
   def draw(self):
      print ('Drawing Circles')

# Creating the object of Rectangle class
rect=Rectangle()

# Creating the object of Circle class
cir=Circle()

# Creating the object of Shape class [Base class]
sh=Shape()

print('Python Runtime polymorphism Output')
# calling the draw method from Shape class
sh.draw() 

# Assigning the Reference of the Rectangle class to Shape class
sh=rect
sh.draw()   # calls the draw method from the Rectangle class

# Assigning the Reference of the Circle class to Shape class
sh=cir
sh.draw()  # calls the draw function from the Circle class

