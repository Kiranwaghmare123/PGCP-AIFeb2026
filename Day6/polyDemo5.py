class A:
    def m1(self):
        print("Class A: m1()")
        
class B:
    def m1(self):
        print("Class B: m1()")
        
def call(obj):
    obj.m1()
    
call(A())
call(B())
    