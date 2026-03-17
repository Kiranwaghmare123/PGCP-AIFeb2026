from abc import ABC, abstractmethod

class A(ABC):
    @abstractmethod
    def m1(self):
        pass
            
class B(A):
   pass

#a = B() Error :TypeError: Can't instantiate abstract class B without an implementation for abstract method 'm1'
