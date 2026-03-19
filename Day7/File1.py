f = open("abc.txt", "r")
data = f.read(15)
print(data)
print()

data1 = f.readline()
data2 = f.readline()
data3 = f.readline()

print(data1)
print(data2)
print(data3)

line = f.readlines()
print(line)

for line in f:
    print(line.strip()) #removes extra newline
f.close()
