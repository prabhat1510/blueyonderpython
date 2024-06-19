# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 14:06:08 2024

@author: UD SYSTEMS
"""

# Example - Mobile class

class Mobile:  
     #parameterized constructor
     def __init__(self, IEMICode,SIMCard,Processor,IM,IsSingleSIM):
              self.IEMICode=IEMICode
              self.SIMCard=SIMCard
              self.Processor=Processor
              self.IM=IM
              self.IsSingleSIM=IsSingleSIM

         # Methods 
     def GetIEMICode(self):  
              print(self.IEMICode)
   
     def Dial(self):  
           print("Dial a number")  
    
     def Receive(self):  
           print("Receive a call") 
     
     def SendMessage(self):  
           print("Message Sent")

def Main():
         #create the object of the Mobile class
         objM1=Mobile("IER01", "Airtel","4GB","400MB",False)

         #calling the object
         objM1.GetIEMICode()
         objM1.Dial()
         objM1.Receive()
         objM1.SendMessage()

# Main
if __name__ == '__main__':
         Main()