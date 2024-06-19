# Python Multiple Inheritance Example

#Base class declaration
class A1:
     
    def __init__(self,num):
        self._num=num
    
    def a1Method(self):
        print("Inside class A1" )
        

#Base class declaration
class B1:

    def __init__(self,num1):
        self._num1=num1
    def b1Method(self):
        print("Inside class B1" )

#Derived class declaration
class C1(A1, B1):
      def __init__(self,n,n1):
          A1.__init__(self, n)# calling the A1 Base class constructor
          B1.__init__(self, n1)# calling the B1 Base class constructor

      def findSum(self):
          return self._num+self._num1


        
#creating the object of the Subclass
print("Example - Multiple Inheritance ")
objC=C1(20,30)
sum=objC.findSum()
print("Total : ", sum)
objC.a1Method()
objC.b1Method()
