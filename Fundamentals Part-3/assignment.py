# Q1 — Check Palindrome String
# s = input("Enter a string: ")
# rev = ""
# for ch in s:
#     rev = ch + rev
# if s == rev:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# # Q2 — Student Dictionary Menu
# students = {}
# while True:
#     print("\nA-Add  B-Update  C-Search  D-Display  E-Exit")
#     ch = input("Enter choice: ")
#     if ch == 'A':
#         name = input("Student name: ")
#         marks = int(input("Marks: "))
#         students[name] = marks
#     elif ch == 'B':
#         name = input("Student name to update: ")
#         marks = int(input("New marks: "))
#         students[name] = marks
#     elif ch == 'C':
#         name = input("Student name: ")
#         print(students.get(name, "Not found"))
#     elif ch == 'D':
#         print(students)
#     elif ch == 'E':
#         break

# Q3 — Word Length Dictionary
# words = ["apple","banana","kiwi","cherry","mango"]
# d = {}
# for w in words:
#     d[w] = len(w)
# print(d)

# Q4 — Count Spaces in String
# s = input("Enter a string: ")
# count = 0
# for ch in s:
#     if ch == " ":
#         count += 1
# print("Spaces =", count)

# Q5 — Unique Characters
# s = input("Enter a string: ")
# unique = set(s)
# print("Unique characters:", unique)
# print("Count:", len(unique))