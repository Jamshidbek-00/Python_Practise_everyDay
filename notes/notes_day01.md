## Day 1 - Variables

What I learned:
- Variables store data
- Use = to assign value
- Python is dynamically typed

Examples:
x = 5
name = "Ali"

Mistakes:
- I tried to start variable with number → error

Fix:
- Variable must start with letter or underscore

Conclusion:
- Variables are easy but naming is important

## Python Output:

- What Python Output Numbers.

--Print Numbers
You can also use the print() function to display numbers:

However, unlike text, we don't put numbers inside double quotes:

Example:
print(3)
print(358)
print(50000)

--Mix Text and Numbers
You can combine text and numbers in one output by separating them with a comma:

Example
print("I am", 35, "years old.")


## Python Comments:
Comments can be used to explain Python code.

Comments can be used to make the code more readable.

Comments can be used to prevent execution when testing code.

Creating a Comment
Comments starts with a #, and Python will ignore them:

Example:
#This is a comment
print("Hello, World!")


## Python Variables

Variables
Variables are containers for storing data values.

Creating Variables
Python has no command for declaring a variable.

A variable is created the moment you first assign a value to it.

Example:
x=5
y="Jama"
print(x)
print(y)

Casting
If you want to specify the data type of a variable, this can be done with casting.

Example
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

-Get the Type
You can get the data type of a variable with the type() function.

x = 7
y = "Apple"

print(type(x))🏁

## ingle or Double Quotes?
String variables can be declared either by using single or double quotes:


## Python - Variable Names

Variable Names
A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume).

Rules for Python variables:

A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.

''' Remember that variable names are case-sensitive '''

# Multi Words Variable Names👆
-Variable names with more than one word can be difficult to read.

-There are several techniques you can use to make them more readable:

-- Camel Case
Each word, except the first, starts with a capital letter:

myVariableName = "John"
-- Pascal Case
Each word starts with a capital letter:

MyVariableName = "John"
-- Snake Case
Each word is separated by an underscore character:

my_variable_name = "John"

## Many Values to Multiple Variables

Python allows you to assign values to multiple variables in one line:
Note: Make sure the number of variables matches the number of values, or else you will get an error.


----One Value to Multiple Variables
And you can assign the same value to multiple variables in one line:

Example
x = y = z = "Orange"
print(x)
print(y)
print(z)

-- Unpack a Collection

## Python - Output Variables
Notice the space character after "Python " and "is ", without them the result would be "Pythonisawesome".

