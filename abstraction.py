#Abstraction in poython
from abc import ABC, abstractmethod


class Wallets(ABC):
    
 @abstractmethod
 def pay(self):
        print("Test")
        pass
    
 class Paypal(Wallets):
    def pay(self):
        print("Paypal payment")
        
    def displayInfo():
         Wallets.pay()
         
    
    obj = Paypal
    obj.displayInfo()
        
    
 