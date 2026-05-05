## 🟢 Python Strings

🔹 String nima?

String (str) — bu matn.

Note: in the result, the line breaks
are inserted at the same position as in the code.

## 🟢 Strings are Arrays

Python’da string aslida harflardan iborat ketma-ketlik (array/sequence).

👉 Ya’ni:

string ichidagi har bir belgi alohida element hisoblanadi

example:
P   y   t   h   o   n
0   1   2   3   4   5

🟢 Loop bilan ishlash:
text = "Python"

for letter in text:
    print(letter)
👉 Har bir harfni alohida chiqaradi


🟢 Index orqali olish:
text = "Python"

print(text[0])  # P
print(text[1])  # y

🟢 Loop bilan ishlash
text = "Python"

for letter in text:
    print(letter)

🟢 Len() — uzunligi:
text = "Python"
print(len(text))

🟢 Slicing (kesish)
text = "Python"

print(text[0:3])  # Pyt
print(text[2:5])  # tho

🟢 Xulosa

* String = harflar ketma-ketligi (array kabi)
* Har bir elementga index orqali murojaat qilinadi
* Loop bilan ishlash mumkin
* O‘zgartirib bo‘lmaydi (immutable)


## Python - Slicing Strings

🟢 Python – Slicing Strings

🔹 Slicing nima?

Slicing — bu string’dan bir qismini kesib olish.

text[start:end]

👉 start → qayerdan boshlansin
👉 end → qayergacha (lekin o‘sha index kirmaydi ❗)

text = "Python"

print(text[0:3])

Step bilan slicing.
text = "Python"

print(text[0:6:2])

F-Strings
Example
Create an f-string:

age = 36
txt = f"My name is John, I am {age}"
print(txt)


## Python - Escape Characters

Example
The escape character allows you to use double quotes when you normally would not be allowed:

txt = "We are the so-called \"Vikings\" from the north."

Escape Characters
Other escape characters used in Python:

Code	Result	Try it
\'	Single Quote	
\\	Backslash	
\n	New Line	
\r	Carriage Return	
\t	Tab	
\b	Backspace	
\f	Form Feed	
\ooo	Octal value	
\xhh	Hex value

# 🟢 Python String Methods (short explanations)

* capitalize()  # birinchi harfni katta qiladi
* casefold()    # hamma harfni kichik qiladi (lower dan kuchliroq)
* center()      # matnni o‘rtaga joylaydi
* count()       # nechta marta takrorlanganini sanaydi
* encode()      # stringni bytes ga o‘tkazadi
* endswith()    # oxiri shu bilan tugaydimi tekshiradi (True/False)
* expandtabs()  # tab (\t) o‘lchamini sozlaydi
* find()        # so‘zni qidiradi, index qaytaradi (-1 bo‘lishi mumkin)
* format()      # string ichiga qiymat qo‘shadi
* format_map()  # format ga o‘xshash, dict bilan ishlaydi
* index()       # find ga o‘xshaydi, lekin topmasa error beradi
* isalnum()     # faqat harf va son bo‘lsa True
* isalpha()     # faqat harf bo‘lsa True
* isascii()     # ASCII belgilar bo‘lsa True
* isdecimal()   # faqat decimal raqamlar bo‘lsa True
* isdigit()     # raqam bo‘lsa True
* isidentifier()# variable nomi bo‘la oladimi tekshiradi
* islower()     # hammasi kichik harfmi
* isnumeric()   # son ekanligini tekshiradi
* isprintable() # chop etiladigan belgilar bo‘lsa True
* isspace()     # faqat bo‘sh joylardan iboratmi
* istitle()     # har so‘z katta harf bilan boshlanadimi
* isupper()     # hammasi katta harfmi
* join()        # list elementlarini stringga qo‘shadi
* ljust()       # chapga tekislaydi
* lower()       # kichik harf qiladi
* lstrip()      # chapdagi bo‘sh joyni olib tashlaydi
* maketrans()   # translate uchun jadval yaratadi
* partition()   # 3 qismga ajratadi (before, sep, after)
* replace()     # matnni almashtiradi
* rfind()       # oxiridan qidiradi
* rindex()      # oxiridan qidiradi (topmasa error)
* rjust()       # o‘ngga tekislaydi
* rpartition()  # oxiridan 3 qismga ajratadi
* rsplit()      # oxiridan bo‘lib beradi
* rstrip()      # o‘ngdagi bo‘sh joyni olib tashlaydi
* split()       # bo‘lib list qaytaradi
* splitlines()  # qatorlar bo‘yicha ajratadi
* startswith()  # boshida shu bormi
* strip()       # bosh va oxirini tozalaydi
* swapcase()    # katta-kichik harflarni almashtiradi
* title()       # har so‘z boshini katta qiladi
* translate()   # belgilarni almashtiradi (maketrans bilan)
* upper()       # katta harf qiladi
* zfill()       # boshiga 0 qo‘shadi

## Python Booleans

🔹 Boolean nima?

Boolean faqat 2 ta qiymatga ega:true and false. yoki 1, or 0

Example
The following will return True:

bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])


Example
The following will return False:

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})


🟢 Functions can Return a Boolean

🔹 Nazariy tushuncha

Funksiya faqat son yoki matn emas, balki True yoki False (Boolean) ham qaytara oladi.

👉 Ya’ni:

funksiya natijasi “ha” yoki “yo‘q” bo‘lishi mumkin

Operators:
Python Arithmetic Operators
Arithmetic Operators
Arithmetic operators are used with numeric values to perform common mathematical operations:

Operator	Name	Example
+	Addition	x + y	
-	Subtraction	x - y	
*	Multiplication	x * y	
/	Division	x / y	
%	Modulus	x % y	
**	Exponentiation	x ** y	
//	Floor division	x // y	

Assignment Operators
Assignment operators are used to assign values to variables:

* Operator	Example	Same As	Try it
* =	x = 5	x = 5	
* +=	x += 3	x = x + 3	
* -=	x -= 3	x = x - 3	
* *=	x *= 3	x = x * 3	
* /=	x /= 3	x = x / 3	
* %=	x %= 3	x = x % 3	
* //=	x //= 3	x = x // 3	
* **=	x **= 3	x = x ** 3	
* &=	x &= 3	x = x & 3	
* |=	x |= 3	x = x | 3	
* ^=	x ^= 3	x = x ^ 3	
* >>=	x >>= 3	x = x >> 3	
* <<=	x <<= 3	x = x << 3	
* :=	print(x := 3)	x = 3
* print(x)	


