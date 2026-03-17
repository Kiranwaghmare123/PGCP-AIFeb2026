from abc import ABC,abstractmethod

class A(ABC):  # Abstract class
    @abstractmethod
    def m1(self): # Abstract method
        pass
        
class B(A): 
    def m1(self): # Abstract method is implemented
        print("m1(): implemented in child class")
        
a = B()
a.m1() 