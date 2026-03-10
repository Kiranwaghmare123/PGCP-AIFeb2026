# Type Casting:

#int()
print(int(123)) 
print(int(123.3456)) 
print(int(True))
#print(int(12+5j))  
#print(int("Hello")) 
print(int("12345")) 
print(type("12345")) 

#float()
print(float(123)) 
print(float(123.3456)) 
print(float(True))
#print(float(12+5j))  : TypeError: float() argument must be a string or a real number, not 'complex'
#print(float("Hello")) : ValueError: could not convert string to float: 'Hello'
print()

#complex()
#int()
print(complex(123)) 
print(complex(123.3456)) 
print(complex(True))
print(complex(True,True))
print(complex(12+5j))  
#print(complex("Hello")) :  ValueError:

print()
