# Python-day01🧑‍💻:

# 1. ikki sonni qo‘sh
a = 5
b = 7
print(a + b)

# 2. ism va yosh chiqar
name = "Jamshid"
age = 20
print("My name is", name)
print("I am", age)

# 3. 3 ta sonni ko‘paytir
x, y, z = 2, 3, 4
print(x * y * z)


# Python-day02:

username = "jamshid"
password = "12345"

print("Login:", username)

# ex:
name = "Jamshidbek"
university = "TATU"

print(f"My name is {name} and I study at {university}")

# 🟢 Global keyword bilan global variable ni o‘zgartirish

# ex01:
balance = 100_000
def add_money():
    global balance
    balance += 50_000
add_money()
print(f"Total balance: {balance}")



# Python Data Types:
# *******


# 🟢 Python Strings

# 🔹 String nima?
# String (str) — bu matn.

# exercises:
# *
text = "pythonprogramming"
print(text[:6])
print(text[6:])
print(text[::-1])

# *
text = " Jamshidbek  "
print(text.strip())

