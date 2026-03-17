class A:
    def m1(self):
        print("Class A : m1()")
        
class B(A):
    def m1(self):
        print("Class B : m1()")
        
s = B()
s.m1()

s = A()
s.m1()