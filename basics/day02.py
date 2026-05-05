# Python - Global Variables
from idlelib.configdialog import changes

# python types
x = 10          # int (butun son)
y = 3.14        # float (kasr son)
name = "Ali"    # string (matn)
is_ok = True    # boolean

username = "jamshid"
password = "12345"

print("Login:", username)

# ex:

name = "Jamshid"
university = "TDTU"
print(f"My name is {name} and I study at {university}")

# ex:
x = 7
def change():
    global x
    x = 11
change()
print(x)

# exercise:
x = "awesome"
def myfunc():
    print("Python is" " "+ x)
myfunc()

# 2-ex
x = 'awesome'
def my_func():
    x = "fantastic"
    print("Python is " + x)

my_func()
print("Python is " + x)


# Global keyword?

def test():
    global x
    x = "Jamshid"
test()
print("My name is " + x)


# Python Data Types
# 🟢 Python Data Types (ma’lumot turlari)
#
# 🔹 1. Data type nima?
#
# Data type — bu o‘zgaruvchi ichida qanday turdagi ma’lumot saqlanayotganini bildiradi.
#
# Oddiy qilib:
#
# variable ichida nima borligini aytadi



# 🟢 Python Numbers
# Python’da numbers (sonlar) 3 ta asosiy turga bo‘linadi:

#Task:
# 1
x = 10
y = int(x)
print(y + 10)

#2- random son chiqarish
import random
x = random.randint(1, 100)
print(x)


import random
print(random.randrange(1, 10))


# 🟢 Python Casting
# 🔹 Casting nima?
# Casting — bu bir data type’ni boshqa data type’ga o‘tkazish.

x = int(5.0)
print(x)

a = float(2)
print(a)

b = str(100)
print(b)