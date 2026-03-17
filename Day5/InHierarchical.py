class A:
    def m1(self):
        print("m1() : parent class 1")
        
class B(A):
    def m2(self):
        print("m2() : child class 1")
        
class C(A):
    def m3(self):
        print("m3() : child class 2")
        
ch1 = B()
ch1.m1()
ch1.m2()
#ch1.m3()

ch1 = C()
ch1.m1()
#ch1.m2()
ch1.m3()

ch1 = A()
ch1.m1()
#ch1.m2()
#ch1.m3()