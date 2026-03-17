class A:
    def __init__(self):
        print("Constructor : class A")
    def m1(self):
        print("Class A : m1()")
        
class B(A):
    def __init__(self):
        super().__init__()
        print("Constructor : class B")
    def m1(self):
        print("Class B : m1()")
        
s = B()
s.m1()