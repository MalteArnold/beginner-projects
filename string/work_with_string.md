# Working with `string`
Here we are going to some functions and methods to use the data type string.
A string is generally considered a data type and is often implemented as an array data structure of bytes (or words) that stores a sequence of elements, typically characters, using some character encoding.
### Store string in variable
```
string = "Hello my name is Joe"
```
### Testing data type with `type()` and displaying it using `print()`
```
print(type(string))
```
Strings are fundamentally immutable. After creating a string object, individual characters cannot be altered.
But we can store the modified string in a new variable. More on that later.
### Accessing individual characters (index) starting from 0, ending at -1 and displaying it using `print()`
```
print(string[0])
print(string[-1])
```
### Slice the sting and displaying it using `print()`
```
print(string[1:-3]) # Character 2 to the third-to-last
print(string[:6]) # Character 1 to 7
print(string[-3:]) # Character third-to-last to last
```
### Combining strings to create a new string
```
string_2 = string + " and i am living in New York"
```
### Combining a part of a string to create a new string
```
string_3 = "Hola " + test[6:] # changes `Hello` to `Hola`
```
### Joining strings using `.join()` and displaying it using `print()`
```
str1 = "I am living in the USA"
str2 = "I was born in Germany"
str3 = " but ".join([str1, str2])
print(str3)
```
### Querying the length of a string with `len()` and displaying it using `print()`
```
print(len(str3))
```
### Counting a specific character in a string using `.count()` and displaying it using `print()`
```
print(str3.count("a"))
```
### Determining if a character is present or not using the `in` function and displaying it using `print()`
```
print("India" in str3) # False
print("Germany" in str3) # True
```
### Finding the index of a specific character using `.find()`
```
str3.find("l")
str3.find("born")
```
Case sensitivity matters, and you can search for the starting index of a whole word or more.
### Using the `find()` function as an aid for slicing
```
str3[str3.find("bin"):]
str3[:str3.find("bin")]
```
### Changing a string to uppercase using `.upper()`
```
str3.upper()
```
### Changing a string to lowercase using `.lower()`
```
str3.lower()
```
This can be useful, for example, if you are searching for a character and are unsure whether it's in uppercase or lowercase.
### Changing characters using `.replace()` and displaying it using `print()`
```
print("Hallo".replace("a", "e"))
```
### Breaking down into individual elements using `.split()`
```
str4 = str3.split("i")
```
### Removing leading and trailing spaces using `.strip()`
```
str_strip = " Hello ".strip()
```
### Dynamically generating a string using `.format()` and displaying it using `print()`
```
print("1. character: {}, 2. character: {}".format(str3[0], str3[1]))
# or
print(f"1. Zeichen: {str3[0]}, 2. Zeichen: {str3[1]}")
