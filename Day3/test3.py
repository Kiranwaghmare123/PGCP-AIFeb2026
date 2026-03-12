#Find largest number in list

n = [12,34,67,89,36,78,66,11]
        
largest = n[0]

for num in n:
    if num > largest:
        largest = num
        
print("Largest=", largest)