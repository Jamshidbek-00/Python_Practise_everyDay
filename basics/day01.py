# Variables - examples

# string
name = "Jamshid"

# integer
age = 20

# float
price = 10.5

print(name)
print(age)
print(price)

# changing value
age = 21
print(age)

# Print Numbers:
print(3)
print(358)
print(50000)

# 2-ex

print(3+4)
print(40-23)

# Python Comments
#Python variables:
x = 5
y = "Jamshid"
print(x, end=", ")
print(y)


# Casting

x = int(3)
y = float(3)
z = str(3)
print(x)
print(y)
print(z)

# Get a data type.

x = 7
y = "Apple"

print(type(x))

# Python Variable names
# Legal variable name

name = "Jamshid"
Name = "Jamshid"
_name = "Jamshid"
my_name = "Jamshid"
NAME = "Jamshid" # These is rule in python variable name.Its true.

# Illegal variable nam:
# 2name = "Muhammadali"
# my-name = "Muhammad ali"
# my name = "Muhammad ali"
# print(2name)
# print(my-name)
# print(my name)


''' Many Values to Multiple Variables
Python allows you to assign values to multiple variables in one line:

Example:

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z) '''

x, y, z = 20, "Apple", "Car"

print(x)
print(y)
print(z)


# One Value to Multiple Variables
x = y = z = "Banana"
print(x)
print(y)
print(z)

# Unpack a Collection
fruits = "Banana", "apple", "cherry"
x, y, z = fruits
print(x,y,z)
print(x)
print(y)
print(z)


# Python - Output Variables

x = 10          # int (butun son)
y = 3.14        # float (kasr son)
name = "Ali"    # string (matn)
is_ok = True    # boolean