#Separate positive and negative numbers

n1 = [12,34,-67,89,-36,78,-66,11,-34,78,-12,12,12,36,89]
        
p = []
n = []

for num in n1:
    if num >= 0:
        p.append(num)
    else:
        n.append(num)
        
print("Positive list:",p)
print("Negative list:",n)
       