list = [10,20,304,40,50]
print(list)

#Ordered
print(list)

#Mutuble
print(list[0])
list[0] = 777
print(list)

list = [10,20,304,40,50,304,304,304,10]
print(list)


list = [10,20.45,304,4067,50,304.78,304,304,10,"Kiran",'CDAC',True,None]
print(list)

a =[]
print(a)
print(type(a))
print(id(a))

list = [10,20,(304,40,50,304),304,304,10]
print(list)

list = [10,20,[304,40,50,304],304,304,10]
print(list)

list = [10,20,[304,[40,50],304],[304],304,10]
print(list)

list = [10,20,304,40,50,304,304,304,100]
print(list[0])
print(list[-1])
print(list[-5])

list = [10,20,[304,[40,50],303],[301],304,10]
print(list[0])
print(list[2][0])
print(list[3][0])
#print(list[3][1]) :IndexError: list index out of range
print(list[2][1])

#Slicing

list = [10,20.45,304,4067,50,304.78,304,304,10,"Kiran",'CDAC',True,None]
print(list[1:4])
print(list[:4])
print(list[5:7])
print(list[:4])
print(list[:-1])
print(list[6:-3])
list[2] =777
print(list)
list[1:5] =[11,222,33,444]
print(list)

list.append("Python")
print(list)
list.append([3,4,5,6])
print(list)

list.extend([13,14,15,16])
print(list)

list.extend("CDAC")
print(list)

list.insert(100,200)
print(list)

list.insert(0,1000)
print(list)

list.remove(1000)
print(list)

list.pop()
print(list)

list.pop(2)
print(list)

print(list.index(10))

print(list.count(304))

print(list.reverse())
print(list)

a= [11,2,5,9,3]
a.sort()
print(a)

a.sort(reverse=True)
print(a)


#del list[1]

#list.clear()
#print(list)

