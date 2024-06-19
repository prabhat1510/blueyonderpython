# Python Hierarchial Inheritance Example
#Base class declaration



class Account:
   def __init__(self,accno, acnm):
        self._accno=accno
        self._accname=acnm

#Derived class declaration
class SBAcct(Account):
    def __init__(self,accno,acnm,minbal):
        Account.__init__(self,accno,acnm) #calling the base class constructor
        self.minbal=minbal

    def showSBInfo(self):
       print("SB Account Information")
       print("Account no :", self._accno)
       print("Current Balance :", self.minbal)



class Loan(Account):
    def __init__(self,accno,acnm,loanamt,term):
        Account.__init__(self,accno,acnm) #calling the base class constructor
        self.loanamt=loanamt
        self.term=term

    def showLoanInfo(self):
       print("Loan Account Information")
       print("Account no :", self._accno)
       print("Loan Amount :", self.loanamt)


#creating the object of the Subclass
print("Example - Hierarchical Inheritance ")
objsb1=SBAcct(2004, "Sanjay", 4000.00)
objsb1.showSBInfo()

objLoan1=Loan(2005, "Sanjay", 10000.00, 3)
objLoan1.showLoanInfo()






