class A:
    def m1(self, *args):
        print("Arguments are :", args)
        
a1 = A()
a1.m1()
a1.m1(10)
a1.m1(10,20,30,30)        