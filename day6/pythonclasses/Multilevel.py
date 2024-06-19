# Python Multilevel Inheritance Example
#Base class declaration
class Account:
    
    def __init__(self,accno, acnm):
        self.accno=accno
        self.accname=acnm

#Derived class declaration
class SBAcct(Account):
    def __init__(self,accno,acnm,minbal):
        Account.__init__(self,accno,acnm) #calling the base class constructor
        self.minbal=minbal

#Derived class declaration
class Transaction(SBAcct):
    def __init__(self,accno,acnm,minbal):
        SBAcct.__init__(self,accno,acnm,minbal) #calling the base class constructor
    
    def deposit(self, amt):
        self.minbal=self.minbal+amt  # adding the amount to the balance

    def withdraw(self, amt):
        self.minbal=self.minbal-amt  # Subtracting the amount from the balance
      
    def showBalance(self):
        print("Current Balance :", self.minbal)

#creating the object of the Subclass
print("Example - Multilevel Inheritance")
objsb1=Transaction(2004, "Sanjay", 4000.00)
objsb1.showBalance()

#call the deposit function
objsb1.deposit(2000)
print("Balance after Deposit")
objsb1.showBalance()


#call the withdraw function
objsb1.withdraw(2500)
print("Balance after withdraw")
objsb1.showBalance()

