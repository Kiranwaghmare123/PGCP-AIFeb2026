#Complex number = a + bj, j=sqrt(-1)

a = 3 + 5j
b = 10 + 5.5j
c = 2.5 + 4.3j
d = 2.5 + 4j


print(type(a))
print(a)

print(type(b))
print(b)

print(type(c))
print(c)

print(type(d))
print(d)

#-------------------
c = 0B111 + 5j
print(type(c))
print(c)

c = 0o111 + 5j
print(type(c))
print(c)

c = 0xA11 + 5j
print(type(c))
print(c)

#--------------------
#c = 3 + 0B111j # syntax error
#print(type(c))
#print(c)

#-------------
a = 10 + 1.5j
b = 20 + 2.4j


c = a + b
print(type(c))
print(c)

print(a + b)
print(c)

print(a - b)
print(c)

print(a * b)
print(c.real)
print(c.imag)