a = 10
name = "CDAC"
name1 = "CDAC"
 
print(id(a))
print(id(name))
print(id(name1))

name = name1
print(id(name))
print(id(name1))

name = "CDAC!"