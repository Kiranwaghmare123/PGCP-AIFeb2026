
#Accessing character:
s = "CDACMUMBAI-1"
print(s[-5]) # U
print(s[5])
print(s[-0])
print(s[0])  
print(s[10]) 
# print(s[15]) : IndexError: string index out of range
    
    
#String Slicing:
#string[start:end-1]
s = "CDACMUMBAI-1"
print(s[1:4])
print(s[1:])
print(s[:4])
print(s[:])

print(s *3)
print("Aditya" *5)
print(len(s))