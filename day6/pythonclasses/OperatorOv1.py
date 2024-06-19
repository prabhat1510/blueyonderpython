# Python class with + Overloading

#class declaration
class Sample:

    # constructor declaration
    def __init__(self,num1):
        self.num1=num1
    
    #overloaded method
    def __add__(self,other):
        s = self.num1 + other.num1
        print("Sum = : ", s)

    def getNum(self):
        return self.num1
 

#object creation
a1=Sample(20)
a2=Sample(50)

print("Python Example Operator Overloading  : ")
print("First No. :", a1.getNum())
print("Second No. :", a2.getNum())

# calling overloaded method
a1 + a2






