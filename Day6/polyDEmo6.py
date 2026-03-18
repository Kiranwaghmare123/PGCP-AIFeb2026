class A:
    def m1(self):
        print("Class A: m1()")
        
class B(A):
    def m1(self):
        print("Class B: m1()")
        
class C(A):
    def m1(self):
        print("Class C: m1()")
        
obj = [B(), C()]
for o1 in obj:
    o1.m1() 