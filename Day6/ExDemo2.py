
try:
    print("start......")
    a = int(input())
    b = int(input())
    print(a/b)
    print("stop......")
except ArithmeticError:
    print("Cannot divide by zero")
else:
    print("No exception")
finally:
    print("Always executed")
    
print("end......")