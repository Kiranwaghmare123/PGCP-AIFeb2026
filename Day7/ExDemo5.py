
try:
    print("start......")
    num = int(input("Enter index"))
    list = [10,202,30]
    print(list[num])
    
    print("try......")
except ValueError:
    print("Enter number")
    print("except......1")
    
except IndexError:
    print("Enter valid index")
    print("except......2")

    
print("end......")