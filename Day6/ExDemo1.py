n = 10
try:
    print("start......")
    res = n / 0
    print("stop......")
except ZeroDivisionError:
    print("Cannot divide by zero")
    
print("end......")