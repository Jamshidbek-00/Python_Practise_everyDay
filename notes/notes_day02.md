## Python - Global Variables

Types:
x = 10          # int (butun son)
y = 3.14        # float (kasr son)
name = "Ali"    # string (matn)
is_ok = True    # boolean

example:
username = "jamshid"
password = "12345"

print("Login:", username)

* 🟢 Global Variables (oddiy tushuncha)
* 
* Global variable — bu funksiyadan tashqarida yaratilgan o‘zgaruvchi.
* U dasturdagi hamma joyda ishlatilishi mumkin.
* ex:
x = 10  # global variable

def show():
    print(x)

show()

Global variable.
🔹 Xulosa

* Global variable → hamma joyda ishlaydi
* global → qiymatini o‘zgartirish uchun kerak
* Ko‘p ishlatish yaxshi emas (kod chalkash bo‘ladi)


## Global keyword bilan global variable ni o‘zgartirish

🔹 Asosiy g‘oya

Agar global variable bor bo‘lsa va uni funksiya ichida o‘zgartirmoqchi bo‘lsang,
👉 global yozishing SHART


## Python Data Types:
Built-in Data Types
In programming, data type is an important concept.

Variables can store data of different types, and different types can do different things.

[ ] Python has the following data types built-in by default, in these categories:
1. Text Type:	str
2. Numeric Types:	int, float, complex
3. Sequence Types:	list, tuple, range
4. Mapping Type:	dict
5. Set Types:	set, frozenset
6. Boolean Type:	bool
7. Binary Types:	bytes, bytearray, memoryview
8. None Type:	NoneType

# 🟢 Python built-in data types

# Text → str  # Matn saqlash uchun ishlatiladi (string)
# Example: "Hello", "Jamshidbek"

# Numbers → int, float, complex  
# int → butun son (10, -5)  
# float → kasr son (3.14, 10.5)  
# complex → kompleks son (2 + 3j)

# Sequence → list, tuple, range  
# list → o'zgaradigan ro'yxat ["apple", "banana"]  
# tuple → o'zgarmaydigan ro'yxat (1, 2, 3)  
# range → sonlar ketma-ketligi range(5)

# Mapping → dict  
# dict → key-value (kalit-qiymat) saqlaydi  
# Example: {"name": "Jamshidbek", "age": 20}

# Set → set, frozenset  
# set → takrorlanmaydigan qiymatlar {1, 2, 3}  
# frozenset → o'zgarmaydigan set

# Boolean → bool  
# bool → True yoki False qiymatlar

# Binary → bytes, bytearray, memoryview  
# bytes → o'zgarmas binary data  
# bytearray → o'zgaradigan binary data  
# memoryview → memoryni ko'rish uchun

# None → NoneType  
# None → bo'sh qiymat, hech narsa yo'q degani

🟢 Python Data Types (ma’lumot turlari)

🔹 1. Data type nima?

Data type — bu o‘zgaruvchi ichida qanday turdagi ma’lumot saqlanayotganini bildiradi.

Oddiy qilib:

variable ichida nima borligini aytadi

`🟢 Python Numbers

Python’da numbers (sonlar) 3 ta asosiy turga bo‘linadi: int, float, complex.
`

🟢 Xulosa

Python Numbers:

* int → butun son
* float → kasr son
* complex → murakkab son
* random → tasodifiy son

* Int
* Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.

* Float
* Float, or "floating point number" is a number, positive or negative, containing one or more decimals.

Example
Floats:

x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

**Note: You cannot convert complex numbers into another number type.**

* 🟢 Python Casting

* 🔹 Casting nima?
* 
* Casting — bu bir data type’ni boshqa data type’ga o‘tkazish.
* 
* Oddiy qilib:
* 
* “sonni matnga, matnni songa aylantirish”


