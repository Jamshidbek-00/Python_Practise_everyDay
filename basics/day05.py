# append()

thisList = ["banana", "apple", "pear",]
thisList.append("melon")
thisList.insert(1, "cherry")
print(thisList)

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
# thislist.append(tropical)
print(thislist)

# loop
people = ["Muhammad ali", "Abdulloh", "Fayizbek", "Xojiakbar"]
for x in people:
    print(x)

# Index boyicha
ismlar = ["Muhammad ali", "Abdulloh", "Fayizbek", "Xojiakbar"]
for i in range(len(ismlar)):
    print(f"{i} - o'rinda {ismlar[i]} turibdi")


# while
names = ["Muhammad ali", "Abdulloh", "Fayizbek", "Xojiakbar"]
i = 0
while i < len(names):
    print(names[i])
    i += 1

mevalar = ["olma", "banan", "olcha", "qovun"]

i = 0  # Sanoqchi boshlang'ich nuqtasi (indeks 0 dan boshlanadi)

while i < len(mevalar): # Toki i mevalar sonidan kichik ekan...
    print(mevalar[i])   # Ro'yxatning i-elementini ko'rsat
    i = i + 1           # Sanoqchini 1 taga oshir (keyingi elementga o'tish)


sonlar = [1, 2, 3, 4, 5]
kvadratlar = []

for x in sonlar:
    kvadratlar.append(x*x)
print(kvadratlar)

# list comprehention
sonlar = [5, 6, 7, 8, 9]
kvadrat = [x*x for x in sonlar]
print(kvadrat)
# 4. Qanday o'qiladi?
#
# Sintaksisni tushunish uchun uni o'ngdan chapga qarab o'qing:
#
# for x in sonlar — "sonlar ichidagi har bir x uchun..."
#
# x * x — "...uni o'ziga ko'paytir..."
#
# [...] — "...va natijani yangi ro'yxatga yig'."


# 5. Murakkabroq: Shart (if) qo'shish
#
# List comprehension ichida hatto if (shart) ham ishlatsa bo'ladi. Masalan, faqat juft sonlarni ajratib olmoqchimiz:

sonlar = [1, 2, 3, 4, 5, 6]
juft_sonlar = [x for x in sonlar if x % 2 == 0]

print(juft_sonlar) # [2, 4, 6]

numbers = [3, 5, 4, 3, 8, 6, 8, 7, 9]
juft_son = [x for x in numbers if x%2 == 0]
print(juft_son)

name = ["ali", "abdulloh"]
bosh_harf = [n.capitalize() for n in name]
print(bosh_harf)

foydalanuvchilar = ["  ali ", " vali", "olim  "]

# .strip() - bo'sh joylarni olib tashlaydi
# .title() - birinchi harfni katta qiladi
toza_ismlar = [user.strip().title() for user in foydalanuvchilar]

print(toza_ismlar)
# Natija: ['Ali', 'Vali', 'Olim']

# Sets;
cars = {"bmw", "byd", "mercedes", "toyotto"}
print(cars)

thisset = {"apple", "banana", "cherry", True, 1, 2, 3}

print(thisset)


# Dictionaries:
car = {
    "Brand" : "Tracker",
    "Model" : "Gentra",
    "Year" : "2022"
}
print(car)


men = {
    "Ism" : "Jamshid",
    "Yosh" : 21,
    "Shahar" : "Fergana city"
}
print(men)
print(men["Yosh"])
x = men.keys()

men["Surname"] = "Mardonov"
print(x)
y=men.items()
print(y)





