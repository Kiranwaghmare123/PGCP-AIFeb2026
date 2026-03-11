# Arithmetic operator:
    
a = 10
b = 5
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)
print(a//b)

# Assignment oprator

x = 5
x += 5
x -= 3
x //= 3
x **= 2
print(x)

#Comparison operator

a, b =10,20
print(a==b)
print(a<b)

#Logical operator

age = 26
id = True

print(age >= 24 and id)
print(age >= 24 or id)
print(not id)
print(age >= 24)

#Bitwise operator
#& ,~,`.<<,>>

a = 5  #0101
b = 3  #0011
print(a & b) #0001
# print(a ` b) : SyntaxError: invalid syntax
print(a | b) #0111
print(a ^ b) #0110

print(a << 1) #1010 : 10
print(a >> 1) #0010 : 2
print(a)

a = a << 3
print(a)

print(a << 3) 
print(a >> 3) 

# No increment and decrement operators in python
#print(a++) : SyntaxError: invalid syntax

#Membership operator:
#in : present in given data
#not in    : not present in given data

print()
nums = [10,20,30,40]
print(20 in nums)
print(550 not in nums)
print(40 not in nums)

text = "CDAC Mumbai"
print("Mumbai" in text)
print("MUMBAI" in text)
print("MUMbai" in text)

#Identity operator
#is : same object in memory
#is not : different object

a = [10,20]
b = [10,20]
c = [30,40]
c = a
print()
print(a == b) #values
print(a is b) #different objects
print(a is c)
print(a == c)

print()
x = None
y =""
print(x)
print(type(x))
print(x is None)

print()
print((2**3)**4)

#Ternary Operator
#One line if-else statement

#Syntax: true_vale if condition else else_value

a, b = 10,20
val = a if a < b else b
print(val)