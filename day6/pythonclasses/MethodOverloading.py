# method overloading in python - This will not work on python


#class declaration
class Demo:
      # overloaded function
    def add(self,a,b):
        s=a+b
        print("Sum :", s)
       

    def add(self,a,b,c):
         s=a+b+c
         print("Sum :", s)

#object creation
d1=Demo()

print("Example method overloading")
#calling the overloaded method
d1.add(2,3)
d1.add(4,7,9)
