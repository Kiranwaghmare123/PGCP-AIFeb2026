s ={10,20,30,40,50}
print(s)

s ={10,20,30,40,50,10,10,50}
print(s)

s.add(35)
print(s)

#s ={10,20,30,[40,50]} : TypeError: unhashable type: 'list'
#print(s)

s = set()
print(type(s))


s = set([1,2,3,4])
print(s)
#print(s[0]) : TypeError: 'set' object is not subscriptable
s.add(22)
print(s)
s.add(22)
print(s)

s.update([20,30,40])
print(s)

#s.update([20,30],40): TypeError: 'int' object is not iterable
s.update([20,30],(40,50),{55,66})
print(s)

s.remove(20)
print(s)

s.discard(4)
print(s)

s.pop()
print(s)

s1 = {1,2,3}
s2 = {4,5,6,3}
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
print(s1.symmetric_difference(s2))