name = input("Enter your name: \n")
age = int(input("Enter your age: \n"))

# Method one (comma based)
print("Hi", name, ",your are", age, "years old.")

# Method two (concatenation)
print("Hi " + name + ", your are " + str(age) + " years old.")

# Method three
print(f"Hi {name}, your are {age} years old.")

# Method four
show = "Hi {}, your are {} years old.".format(name, age)
print(show)

# Method five
print("Hi %s, your are %d years old." % (name, age))