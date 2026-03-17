class A:
   
    def m1(self):
        print("Class A : m1()")
        
class B:
    def __init__(self):
        self.s1 = A() # B Has-A A
    def m2(self):
        print("Class B : m2()")
        self.s1.m1()
        
s = B()
s.m2()