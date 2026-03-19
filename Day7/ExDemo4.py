
try:
    print("start......")
    num = int(input("Enter the number"))
    
    values = [100,200,300]
    print(values[num])
    
    print("stop......")
except IndexError:
    print("Index out of range")
except ValueError:
    print("Enter proper integer value")
except Exception:
    print("Enter proper integer value")
else:
    print("No exception")
finally:
    print("Always executed")
    
print("end......")