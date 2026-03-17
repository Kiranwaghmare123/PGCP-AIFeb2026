from abc import ABC, abstractmethod

class A(ABC):
   
    @property
    @abstractmethod
    def m1(self):
        pass
       
class B(A):
    @property
    def m1(self):
       return "m1() : child class implementation"
        

a = B()
print(a.m1)

