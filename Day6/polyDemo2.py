class A:
    def m1(self):
        print("Class A : m1()")
        
class B(A):
    def m1(self):
        print("Class B : m1() : child class")
        
b1 = B()
b1.m1()