from abc import ABC, abstractmethod

class A(ABC):
    
    def __init__(self, name):
        self.name = name
    @abstractmethod
    def m1(self):
        pass
    

        
        
class B(A):
    def m1(self):
        print("m1() : implemented and executed")
        

a = B("Testdata")
a.m1()

