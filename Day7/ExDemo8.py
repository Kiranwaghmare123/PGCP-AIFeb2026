try:
    num = int(input("Enter number: "))
    try :
        print(100/num)
        print("try : Inner")
    except ZeroDivisionError:
        print("Division error")
        print("except : Inner")
        
    print("try : Outter")
except Exception as e:
    print("except",e)
    print("Except : Outer")
else:
    print("else")
finally:
    print("finally")
    