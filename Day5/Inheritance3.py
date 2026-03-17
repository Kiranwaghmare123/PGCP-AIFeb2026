class A:
    def m1(self):
        print("Class A : m1()")
        
class B:
    def m1(self):
        print("Class B : m1()")
        
class C(A,B):
    pass
        
s = C()
s.m1()
print(C.mro())
