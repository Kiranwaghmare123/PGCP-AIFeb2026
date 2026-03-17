from abc import ABC, abstractmethod

class A(ABC):
   
    @staticmethod
    @abstractmethod
    def m1():
        pass
       
class B(A):
    @staticmethod
    def m1():
       print("m1() : child class implementation as class method")
       
a = B()
a.m1()
B.m1()



