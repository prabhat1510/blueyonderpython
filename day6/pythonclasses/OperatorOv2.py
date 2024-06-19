# Python class with > comparsion  Overloading

#class declaration
class Sample:
 
    # function declaration
    def __init__(self,num1):
        self.num1=num1
  
    #overloaded method
    def __gt__(self,other):
        if self.num1 > other.num1:
            print(self.num1, "is Bigger than ", other.num1, "\n")
        else:
            print(self.num1, "is Smaller than ", other.num1, "\n")
    
    def getNum(self):
        return self.num1

#object creation
a1=Sample(20)
a2=Sample(50)

print("Python Example Operator Overloading  : ")
print("First No. :", a1.getNum())
print("Second No. :", a2.getNum())

# calling overloaded method
print("Output for a1 > a2")
a1 > a2

print("Output for a2 > a1")
a2 > a1
