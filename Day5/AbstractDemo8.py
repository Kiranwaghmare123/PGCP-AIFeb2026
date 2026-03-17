from abc import ABC, abstractmethod

class A(ABC):
   
    @classmethod
    @abstractmethod
    def m1(cls):
        pass
       
class B(A):
    @classmethod
    def m1(cls):
       print("m1() : child class implementation as class method")
       
a = B()
a.m1()    
 
B.m1()



