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

a = B()
a.m1()
a.m2()
# b = A() : Error
#b.m1()
#b.m2()