# In this project we want to connect strings and variables to create a madlib
# There are more than one ways to do this

name = "Joe"
location = "New York"
age = 25
birth_month = "August"

# Option 1: 

option1 = "Hello, my name is " + name + ". I am " + str(age) + " years old and I was born in " + birth_month + ". I live in " + location + "."
print(option1)

# Option 2:

option2 = "Hello, my name is %s. I am %d years old and I was born in %s. I live in %s." % (name, age, birth_month, location)
print(option2)

# Option 3:

option3 = "Hello, my name is {}. I am {} years old and I was born in {}. I live in {}.".format(name, age, birth_month, location)
print(option3)

# Option 4:

option4 = f"Hello, my name is {name}. I am {age} years old and I was born in {birth_month}. I live in {location}."
print(option4)
