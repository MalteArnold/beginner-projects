# In this project, we want to work with data in a string

# We want to correct the name and age of a person

# 1. Step: create a string with wrong data
string = "My name is Joe and I am 25 years old"

# 2. Step: replace the wrong data with the correct data
correct_string = string.replace("Joe", "Mike")
correct_string = correct_string.replace("25", "35")

print(correct_string)

# Next we want to get the length of the string

# 1. Step: get the length of the string
length = len(correct_string)

# 2. Step: print the length
print(length)

# Next we want to get just a slice of the string

# 1. Step: slice the string an save it in a variable
name = correct_string[:15]
age = correct_string[-17:]

# 2. Step: print the variables
print(name)
print(age)

# Next we want to count the number of words in the string

# 1. Step: count the number of words
words = correct_string.count(" ") + 1 # +1 because there is no space after the last word

# 2. Step: print the number of words
print(words)

# Next we want to count the letter "a" in the string

# 1. Step: count the letter "a" in the string
a = correct_string.count("a")

# 2. Step: print the number of "a"
print(a)

# At last we want to print the string in uppercase

# 1. Step: print the string in uppercase
print(correct_string.upper())
