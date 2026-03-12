#REverse the list without using reverse()

n = [12,34,67,89,36,78,66,11,34,78,12,12,12]
        
list = []

for num in range(len(n)-1,-1,-1):
        list.append(n[num])
        
print("Reverse list=", list)