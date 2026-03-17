class A:
   
    def m1(self):
        print("Class A : m1()")
        
class B(A):
    def m2(self):
        print("Class B : m2()")
        
s = B()
s.m1()
s.m2()