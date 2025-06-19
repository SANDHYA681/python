#Abstraction in poython
from abc import ABC, abstractmethod


class Wallets(ABC):
    
 @abstractmethod
 def pay():
        print("Test")
        pass
    
 