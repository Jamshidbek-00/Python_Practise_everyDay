""""🟢 Python – Slicing Strings

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
"""

# exercises:
# *
'''matn = "hello python world"
print(matn.replace("python", "django"))
print(matn.upper())
print(matn.split(", "))


name = "Jamshidbek"
age = 20

print("My name is {} and I am {}".format(name, age))'''


# Saturday 23-May 14:17

class EmployeeNode:
    def __init__(self, name):
        self.name = name
        self.right = None
        self.left = None
def find_leaf_employees(root, result_list):
    if root is None:
        return
    if root.left is None and root.right is None:
        result_list.append(root.name)
        return
    find_leaf_employees(root.left, result_list)
    find_leaf_employees(root.right, result_list)
root = EmployeeNode("Anvar")
root.right = EmployeeNode("Bobur")
root.left = EmployeeNode("Zilola")
root.left.left = EmployeeNode("Ali")
root.left.right = EmployeeNode("Vali")
root.right.right = EmployeeNode("Sardor")

quyi_ishchilar = []
find_leaf_employees(root, quyi_ishchilar)
print(quyi_ishchilar)


# Bread Search Algorithm (BSA) - Graph

from collections import deque

