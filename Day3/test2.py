s = {"Amit":80,"Sneha":90,"Raj":60,"Ravi":85,}
print(s)

s["Neha"] = 91
print(s)

s["Raj"] = 82
print(s)

#Search
name = input("Enter name:")

if name in s:
    print("Marks = ", s[name])
else:
    print("Student not found")
    
#Highest Marks
highest = max(s, key=s.get)
print("Highest marks=",highest)
print("Marks=",s[highest])

#Total count of students
print("Total student=",len(s))

# Average marks of student
print("Average marks=",sum(s.values())/len(s))

#Display student above 80 score
for name, marks in s.items():
    if marks > 80:
        print(name)