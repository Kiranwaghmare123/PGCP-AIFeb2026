# Method 1: Using ,

name = "Amit"
sal = 40000
print("Name =", name,"and salary =", sal)

# Method 2: Using operator +
print("Name ="+ name)

# Method 3: Using %
print("Name = %s and salray = %d" % (name,sal))

price = 123.456756
print("price = %f" % price)
print("price = %.2f" % price)
print("price = %.5f" % price)

# Method 4: Using format()
print("Name = {0}, Salary = {1}".format(name, sal))
print("Name = {n}, Salary = {s}".format(n="Rahul", s=30000))


# Method 5: Using f-string
print(f"My name is {name} and salary is {sal}")
x = 1234.56789999
print(f"{x:.2f}")
print(f"{sal:10}")
print(f"{sal:<10}")
print(f"{sal:>10}")
print(f"{sal:^10}")
print(f"{sal:,}")