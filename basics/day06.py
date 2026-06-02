""""# Python Conditions and If statements
from nis import match
from unittest import case

bal = 85

if bal >= 90:
    print("A'lo")
elif bal >=70:
    print("Yaxshi")
else:
    print("Ko'proq o'qish kerak!")

a=5,
b=4,
if a > b: print("a b dan katta")

c =6
d = 6
print("A") if  c > d else print("B")


x = 12

if x != 5:
    print("x 5 ga teng emas")

age = 20
has_id = True
if age > 18 and has_id:
    print("Kirish mumkin")

day = "Saturday"
if day == "Saturday" or "Sunday":
    print("Dam olish kuni")

yosh = 20
if yosh >= 20:
    print("Ruhsat!")
    if yosh >= 21:
        print("To'liq ruhsat!")

num = int(input("Son kiriting: "))
if num % 2 == 0:
    print("Juft son")
else:
    print("Toq son")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
for num in numbers:
    if num % 2 == 0:
        print(num)

score = 90
if score > 90:
    pass
print("Score processed")

# match
# kun_raqami = 3
# match kun_raqami:
#     case 1:
#         print("Dushanba")
#     case 2:
#         print("Seshanba")
#     case 3:
#         print("Chorshanba")
#     case _:
#         print("Bunday kun yo'q")

kun_raqami = 3

if kun_raqami == 1:
    print("Dushanba")
elif kun_raqami == 2:
    print("Seshanba")
elif kun_raqami == 3:
    print("Chorshanba")
else:
    print("Bunday kun yo'q")"""
from basics.day04 import mevalar

#
# parol = ""
# while parol != "1234":
#     parol = input("Parol kiriting: ")
# print("Parol to'g'ri!")
#
# # continue
#
# i = 0
# while i < 5:
#     i += 1
#     if i == 5:
#         continue
#     print(i)
#
# a = 1
# while a < 10:
#     a += 1
#     if a == 5:
#         break
#     print(a)
#     a += 1

# Juft sonlar:
# son = 1
# while son <= 10:
#     print(son)
#     son += 2
#
# num = 1
# while num < 10:
#     print(num)
#     num += 1

# Nested For:
# sifatlar = ["qizil", "shirin"]
# meva = ["olma", "anor"]
# for x in sifatlar:
#     for y in meva:
#         print(x, y)
#
# sonlar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for x in sonlar:
#     if x % 2 == 0:
#         print(x)
#     else:
#         print(f"Toq sonlar: {x}")


# function
def kvadrat(son):
    return son ** 2
natija = kvadrat(5)
print(natija)

def salom_ber(ism):
    print(f"Salom ! {ism}")
salom_ber("Ali")
salom_ber("Abdulloh")
