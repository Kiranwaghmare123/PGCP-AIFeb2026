class A:
    def m1(self):
        print("m1 from class A")

class B:
    def m1(self):
        print("m1 from class B")

def call_method(obj):
    obj.m1()

call_method(A())
call_method(B())