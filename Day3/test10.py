#Merge to sorted list

a = [1,3,5,7,8]
b = [2,6,9]
merge = [] 
i = j = 0

while i < len(a) and j < len(b):
    if a[i] < b[j]:
        merge.append(a[i])
        i+=1
    else:
        merge.append(b[j])
        j+=1
while i < len(a):
    merge.append(a[i])
    i+=1
    
while j < len(b):
    merge.append(b[j])
    j+=1
    
print(merge)