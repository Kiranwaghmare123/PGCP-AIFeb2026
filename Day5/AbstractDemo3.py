from abc import ABC, abstractmethod

class A(ABC):
    @abstractmethod
    def m1(self):
        pass
    
    def m2(self):
        print("m2() : Normal method")
        
        
class B(A):
    def m1(self):
        print("m1() : implemented and executed")
        
    @abstractmethod
    def m3(self):
        pass

a = B()
a.m1()
a.m2()
