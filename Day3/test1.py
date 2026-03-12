#dict = key:value

student = {"name" : "Amit","addr" : "Mumbai", "course" : "AI"}
print(student)

print(student["name"])

#Keys: int, flat, str, tuple, frozenset
# Not allowed: list, set, dictionary

# d ={[1,2]:"a"} : TypeError: unhashable type: 'list'
#print(d)

#dict() : dictionary constructor

d = dict(a=1, b=2, c=3)
print(d)
print()

d = dict([("a",1), ("b",2), ("c",3)])
print(d)

keys = ["id","name","addr"]
values = ["s1","Amit","Mumbai"]

d = dict(zip(keys,values))
print(d)
print()

student = {"name" : "Amit","addr" : "Mumbai", "course" : "AI"}
print(student["name"])
#print(student[age]) #:Error NameError: name 'age' is not defined

print(student.get("name"))
print(student.get("age"))
print(student.get("age","CanNot aval"))
print()

student = {"name" : "Amit","addr" : "Mumbai", "course" : "AI"}
print(student)
student["name"] = "sarika"
print(student)

student = {"name" : "Amit","addr" : "Mumbai", "course" : "AI","name" : "Kavita"}
print(student)


student = {"name" : "Amit","addr" : "Mumbai", "course" : "AI"}
student.update({"name1":"Ravi"})
print(student)

student.update([("name","Ravi"),("addr","Delhi")])
print(student)

student = {"name" : "Amit","addr" : "Mumbai", "course" : "AI"}
student.pop("name")
print(student)

student = {"name" : "Amit","addr" : "Mumbai", "course" : "AI"}
x = student.pop("addr")
print(x)

student = {"name" : "Amit","addr" : "Mumbai", "course" : "AI"}
student.popitem()
print(student)

student.clear()
print(student)

student = {"name" : "Amit","addr" : "Mumbai", "course" : "AI"}
del student["name"]
print(student)

student = {"name" : "Amit","addr" : "Mumbai", "course" : "AI"}
print(student.keys())
print(student.values())
print(student.items())

student = {"name" : "Amit","addr" : "Mumbai", "course" : "AI"}
for k in student:
    print(k)
    
for k in student.values():
    print(k)
    
for k in student.items():
    print(k)
    
s = {"name" : "Amit","addr" : "Mumbai", "course" : "AI"}
s1 = s.copy()
print(s)
print(s1)
print(id(s))
print(id(s1))

s = {"name" : "Amit","addr" : "Mumbai", "course" : "AI"}
s1 = s
print(s)
print(s1)
print(id(s))
print(id(s1))

#//--------------
print()

s = {"name" : "Amit","addr" : "Mumbai", "course" : "AI"}
s1 = s.copy()
s1["name"] = "Ravina"
print(s)
print(s1)
print(id(s))
print(id(s1))

s = {"name" : "Amit","addr" : "Mumbai", "course" : "AI"}
s1 = s
s1["name"] = "Tandon"
print(s)
print(s1)
print(id(s))
print(id(s1))

print()
s = {"name" : "Amit","addr" : "Mumbai", "course" : "AI"}
s.setdefault()


