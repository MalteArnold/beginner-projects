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
