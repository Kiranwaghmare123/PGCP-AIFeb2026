#Count even number

n = [12,34,67,89,36,78,66,11,34,78,12,12,12]
        
list = []

for num in n:
    if num not in list:
        list.append(num)
        
print("Unique list=", list)