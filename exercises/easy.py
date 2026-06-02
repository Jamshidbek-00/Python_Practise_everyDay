"""# Python-day01🧑‍💻:
from xmlrpc.server import resolve_dotted_attribute

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

# Day09-Practice LEET CODE

'''
Given an array of positive integers nums, return an array answer that consists of the digits of each integer in nums after separating them in the same order they appear in nums.
To separate the digits of an integer is to get all the digits it has in the same order.
For example, for the integer 10921, the separation of its digits is [1,0,9,2,1].
 
Example 1:
Input: nums = [13,25,83,77]Output: [1,3,2,5,8,3,7,7]Explanation: 
- The separation of 13 is [1,3].
- The separation of 25 is [2,5].
- The separation of 83 is [8,3].
- The separation of 77 is [7,7].
answer = [1,3,2,5,8,3,7,7]. Note that answer contains the separations in the same order.
Example 2:
Input: nums = [7,1,3,9]Output: [7,1,3,9]Explanation: The separation of each integer in nums is itself.
answer = [7,1,3,9].
 
Constraints:
1 <= nums.length <= 1000
1 <= nums[i] <= 105
'''


# class Solution:
#     def separateDigits(self, nums: List[int]) -> List[int]:
#         answer = []
#
#         for son in nums:
#             matn_shakl = str(son)
#
#             for harf in matn_shakl:
#                 answer.append(int(harf))
#         return answer
"""



''' "Masala Tahlilxonasi" — 1-mashq

Masala: Berilgan matn ichidagi hamma bo'shliqlarni (probel) olib tashlang.

Kirish: "P y t h o n"

Chiqish: "Python" '''

'''
text = "P y t h o n"
result = ""
for i in text:
    if i != " ":
        result += i
print(result)


my_array = [1, 3, 6, 8, 9, 5]
minValue = my_array[0]
maxValue = my_array[0]
for i in my_array:
    if i < minValue:
        minValue = i
    if i > maxValue:
        maxValue = i
print("Lowest value: ", minValue)
print("Max value: ", maxValue)

# yig'indini topish.
array = [1, 2, 3, 4, 5]
sum = 0
for x in array:
    sum += x
print(sum)
'''

# BuBBle sort:
def bubble_sort_temperature(temps):
    n = len(temps)
    for i in range(n):
        for j in range(0, n-i-1):
            if temps[j] > temps[j+1]:
                temps[j], temps[j+1] = temps[j+1], temps[j]
    return temps
haftalik_harorat = [35, 28, 40, 22, 30]
saralangan_harorat = bubble_sort_temperature(haftalik_harorat)
print(saralangan_harorat)

# 2-masala
def sort_wealth(wealth_list):
    n = len(wealth_list)
    for i in range(n):
        for j in range(0, n-i-1):
            if wealth_list[j] < wealth_list[j+1]:
                wealth_list[j], wealth_list[j+1] = wealth_list[j+1], wealth_list[j]
    return wealth_list
prices_list = [150, 900, 50, 1200, 400]
sorted_prices = sort_wealth(prices_list)
print(sorted_prices)


# selection_sorts:
# 3-masala
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i

        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
selection_list = [5, 3, 8, 1, 4]
sorted_list = selection_sort(selection_list)
print(sorted_list)


# 4-masala.
def sort_books(books):
    n = len(books)
    for i in range(n):
        minimum_index = i
        for j in range(i+1, n):
            if books[j] > books[minimum_index]:
                minimum_index = j
        books[i], books[minimum_index] = books[minimum_index], books[i]
    return books

books_list = [250, 120, 340, 90, 200]
sorted_books = sort_books(books_list)
print(sorted_books)

from random import randrange
# Quick sort:
def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array.pop(randrange(len(array)))
        kichik = [i for i in array if i <= pivot]
        katta = [i for i in array if i > pivot]
        print(f"{kichik} + [{pivot}] + {katta}")
        return quick_sort(kichik) + [pivot] + quick_sort(katta)

if __name__ == '__main__':
    array1 = [1, 5, 6, 12, 0, -3, 60]
    print(array1)
    print(quick_sort(array1))



