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
"""
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

# 5-masala:
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
"""

# 6-masala:
# merge sort:
'''
def merge_sort(massiv):
    if len(massiv) <= 1:
        return massiv

    mid = len(massiv) // 2
    left_half = massiv[:mid]
    right_half = massiv[mid:]

    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)

    return merge(sorted_left, sorted_right)
def merge(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

my_array = [3, 8, 4, 0, 5, 9]
print("Natija: ", merge_sort(my_array))
'''

# 7-Masala: "Online Do‘kon: Narxlarni arzonidan qimmatiga saralash"
# Shart: Siz yirik bir online do‘konda backend dasturchisiz. Foydalanuvchi qidiruv tizimidan foydalanganda, mahsulotlarni eng arzonidan boshlab eng qimmatiga qarab (o‘sish tartibida) ko‘rmoqchi bo‘ldi.
# Sizga mahsulotlarning narxlari tartibsiz massiv ko‘rinishida beriladi:
# narxlar = [1200, 450, 2000, 150, 700, 450]
# Siz yuqorida o‘rgangan Merge Sort algoritmidan foydalanib, bu narxlarni tartiblab beruvchi funksiyani yozishingiz kerak.
'''
def online_market(prices):
    if len(prices) <= 1:
        return prices

    mid = len(prices) // 2
    left_half = prices[:mid]
    right_half = prices[mid:]

    # O'zini qayta chaqirib (Rekursiya), bo'laklarni yana maydalaymiz
    sorted_left = online_market(left_half)
    sorted_right = online_market(right_half)

    return merge(sorted_left, sorted_right)
def merge(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

my_prices = [1200, 450, 2000, 150, 700, 450]
print("Tartiblangan narxlar: ", online_market(my_prices))



# 8-Masala:
def quick_sort(massiv):
    if len(massiv) <= 1:
        return massiv
    pivot = massiv[-1]
    left = [x for x in massiv[:-1] if x <= pivot]
    right = [x for x in massiv[:-1] if x > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)
my_list = [4, 2, 9, 1, -1, 22, 5]
print("Tartiblangan quick sort: ", quick_sort(my_list))



def kutubxona(kitoblar):
    if len(kitoblar) <= 1:
        return kitoblar
    pivot = kitoblar[-1]
    left = [x for x in kitoblar[:-1] if x <= pivot]
    right = [x for x in kitoblar[:-1] if x > pivot]
    print(f"{left} + {[pivot]} + {right}")
    return kutubxona(left) + [pivot] + kutubxona(right)

my_books_lists = [2, 4, 6, 666, 888, 99, 0, 11]
print("Tartiblangan kitoblar: ", kutubxona(my_books_lists))


# Binary Search:
# 10-masala:
def binary_search(array, target):
    low = 0
    high = len(array)-1
    while low <= high:
        mid = (low + high) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
lists = [1, 3, 5, 5, 8, 9, 10]
target_value = 8
result_index = binary_search(lists, target=target_value)
print(f"Element: {target_value} fount at index: {result_index}")



# 11-masala
def books(massiv, target):
    l = 0
    h = len(massiv) - 1

    while l <= h:
        middle = (l + h) // 2
        if massiv[middle] == target:
            return middle
        elif massiv[middle] < target:
            l = middle + 1
        else:
            h = middle - 1
    return -1
book_ids = [101, 204, 305, 408, 512, 660, 750, 822, 901]
print(book_ids)
targett = 512
results = books(book_ids, target=targett)
print("Finally result: ", results)



# Binary Search:
def binary_search(numbers, target):
    low = 0
    high = len(numbers)-1

    while low <= high:
        middle = (low+high)//2
        if numbers[middle] == target:
            return middle
        elif numbers[middle] < target:
            low = middle + 1
        else:
            high = middle -1
    return -1
sonlar = [10, 20, 30, 40, 50, 60, 70]
print(sonlar)
maqsad = 60
results = binary_search(sonlar, target=maqsad)
print("Finally: ", results)
'''

# Two pointers:

def two_pointer(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        currently_sum = nums[left] + nums[right]

        if currently_sum == target:
            return [nums[left], nums[right]]
        elif currently_sum < target:
            left += 1
        else:
            right -= 1
    return []

my_nums = [1, 3, 4, 6, 8, 10]
my_target = 13
result = two_pointer(my_nums, target=my_target)
print("Result: ", result)




