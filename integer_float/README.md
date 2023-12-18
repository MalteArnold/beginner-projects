# Data type: `integer` and `float`
Before you start with these projects, you should have knowledge about the `string` data type.
An `integer`, or `int`, is a whole number. It has no decimal point and contains all counting numbers (1, 2, 3, …) as well as their negative counterparts and the number 0. A floating-point number, or a `float`, is a decimal number. It can be used to represent fractional quantities as well as precise measurements.
```
integer = 17
float = 3.5
```
## How to use
Start with the work_with_int_float.md file in this folder. The work_with_int_float.md contains some functions and methods to work with this data type. Get used to this before you start the projects. Every project requires you to code a program to fix a problem. The solution to the projects is in the same .py file. First, try to solve it on your own and only use the solution if you need it.
## Recommended order of projects:
1. shopping_list
2. receipts
# Working with `integer` and `float`
Here we are going to some functions and methods to use the data type integer.
An `integer`, or `int`, is a whole number. It has no decimal point and contains all counting numbers (1, 2, 3, …) as well as their negative counterparts and the number 0.
A floating-point number, or a `float`, is a decimal number. It can be used to represent fractional quantities as well as precise measurements.
### Store `int` and `float` in variables
```
year = 2019
time = 2.5
```
### Testing data type with `type()` and displaying it using `print()`
```
print(type(year))
print(type(time))
```
### Define a float variable without a decimal number
```
def_as_float = float(9)
```
## Calculations
Python performs the arithmetic operations of addition, subtraction, multiplication, and division with +, -, *, and /.
Notice that when we perform division, the result has a decimal place. This is because Python converts all ints to floats before performing division.
```
print(25 * 68 + 13 / 28)
```
Variables that are assigned numeric values can be treated the same as the numbers themselves.
```
width = 8
length = 12
print(width * length)
```
### Calculation with exponents
```
# 8 squared
print(8 ** 2)
# 2 to the 10th power
print(2 ** 10)
```
### Modulo operator
The modulo operator is indicated by % and gives the remainder of a division calculation. If the two numbers are divisible, then the result of the modulo operation will be 0.
```
# Modulo by 2 returns 0 for even numbers and 1 for odd numbers
print(24 % 2)
# Prints 2 because 32 / 3 is 10 with a remainder of 2
print(32 % 3)
```
### Plus equals
Python offers a shorthand for updating variables. When you have a number saved in a variable and want to add to the current value of the variable, you can use the += (plus-equals) operator.
```
total_costs = 0
new_shirt = 50.00
