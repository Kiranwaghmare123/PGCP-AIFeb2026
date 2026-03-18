
try:
    print("start......")
    age = int("hello")
    print(age)
    print("stop......")
except ValueError:
    print("Enter valid integer value")
else:
    print("No exception")
finally:
    print("Always executed")
    
print("end......")