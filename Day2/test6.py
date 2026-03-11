#firse for loop:
    
#for  variable_name in sequence:
#    statements

num = [10,20,30,40,50]
for n in num:
    print(n)
    
for n in "CDAC":
    print(n)
    
for n in 'CDAC':
    print(n)
print()   
for n in "C","D","A","C":
    print(n)
   
num = [10.2,20.3,30.3,40.5,50.6]
for n in num:
    print(n)  
    

for n in range(5):
    print(n)
    
print("Break is over.................. !")

'''range():
    start: default 0 
    stop: excluded
    step: 1
'''
print()
for n in range(5,15):
    print(n)

print()
for n in range(5,150,5):
    print(n)   
print()

print()
for n in range(5,0,-1):
    print(n)   
print()

print()
for n in range(5,0):
    print(n)   
print()