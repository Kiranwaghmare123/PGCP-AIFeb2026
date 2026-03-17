class A:
    def m1(self):
        print("Class A : m1()")
        
class B(A):
    def m1(self):
        super().m1() # Parent class method
        print("Class B : m1()")
        
s = B()
s.m1()

