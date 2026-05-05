'''
🟢 Python Strings

🔹 String nima?

String (str) — bu matn.
'''
from urllib.parse import parse_qsl

# P   y   t   h   o   n
# 0   1   2   3   4   5

# ex:
text = "Jamshid"
print(text[0])

text = "Apple Computer"
print(len(text))

# loop
text = "Assalami alaikum"
for letter in text:
    print(letter)
print(len(text))

txt = "The best things in life are free!"
print("best" in txt)

# Python - Slicing Strings


#Python Boolean tipi:

a = 20
b = 23
if a > b:
    print("A is greater than B")
else:
    print("A is not greater than B")


# 🟢 Functions can Return a Boolean
#
# 🔹 Nazariy tushuncha
#
# Funksiya faqat son yoki matn emas, balki True yoki False (Boolean) ham qaytara oladi.
#
# 👉 Ya’ni:
#
# funksiya natijasi “ha” yoki “yo‘q” bo‘lishi mumkin

# *
def myFunction() :
  return False

print(myFunction())

# *
def my_func():
    return True
if my_func():
    print("Yes")
else:
    print("No")

# *
def check_num(a):
    if isinstance(a, int):
        print("This is a number")
    else:
        print("This is not number")
check_num(10)
check_num("Hello")


# Python Operators
# Python Arithmetic Operators