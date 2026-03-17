from abc import ABC, abstractmethod

class A(ABC):
    
    @abstractmethod
    def m1(self):
        print("m1(): abstract method in parent class")
    
class B(A):
    def m1(self):
        super().m1()
        print("m1() : implemented and executed in child class")
        

a = B()
a.m1()

