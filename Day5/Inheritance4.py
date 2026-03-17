class A:
    def m1(self):
        print("Class A : m1()")
        
class B(A):
    def m1(self):
        print("Class B : m1()")
        
class C(A):
    def m1(self):
        print("Class C : m1()")
        
s = B()
s.m1()
print(C.mro())

s = C()
s.m1()
print(C.mro())
