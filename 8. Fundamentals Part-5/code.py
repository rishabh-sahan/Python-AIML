# f = open("sample.txt", "r") # file object
# f = open("sample.txt", "r")
# f = open("sample.txt", "a") # open the file in append mode
# data = f.read() # read the content of file
# data = f.readline() # read the content of file line by line and store in list
# print(data)
# # print(type(data))

# data = f.readline() # read the content of file line by line and store in list
# print(data)

# f.write("Text to overwrite \nthe complete data.") # write to the file

# f.write("New text being appended\n to the file.") # write to the file

# print(f.read()) # read the content of file

# f.close() # close the file

# f = open("sample2.txt", "x") # create a new file and open it in write mode
# f.write("Some random text")
# f.close()

# f = open("sample.txt", "r+") 
# f.write("123")
# print(f.read())
# f.close()

# f = open("sample.txt", "a+") 
# f.write("123")
# print(f.read())
# f.close()

# f = open("sample.txt", "w+") 
# f.write("123")
# print(f.read())
# f.close()

# with keyword, we don't need to explicitly close the file.
# with open("sample.txt", "r") as f:
#     data = f.read()
#     print(data)
#     print(len(data))

# deleting a file
# import os
# os.remove("sample2.txt") # delete the file

# searching for a word in a file
# data = True
# line = 1
# word = "store"
# with open("sample.txt", "r") as f:
#     while data: 
#         data = f.readline()
#         if(word in data):
#             print(f"{word} found in line {line}")
#             break
#         line += 1
    
# Exception handling
# try:
#     x = int(input("Enter x: "))
#     ans = 10/x
# except ZeroDivisionError:
#     print("Divide by zero is not allowed")
# except ValueError:
#     print("Invalid input, please enter a number")
# else:
#     print(f"ans = {ans}")
# finally:
#     print("This is the end of the python program")

# List comprehensions
# squares = []
# for i in range(6):
#     squares.append(i*i)
# print(squares)

# sq = [i*i for i in range(6) if i%2!=0] # list comprehension with condition
# print(sq)

# nums = [-2, -3, 3, 4, -1, 7]
# nums = [0 if val < 0 else val for val in nums] # list comprehension with condition
# print(nums)

# words = ["python", "hello", "rishabh", "world"]
# # print(words[0].upper()) # convert the first word to uppercase
# words = [val.upper() for val in words] # list comprehension to convert all words to uppercase
# print(words)

# JSON module
# import json
# py_obj = {
#     "name": "Rishabh",
#     "is_student": True,
#     "address": None
# }   

# json_str = '{"name": "Rishabh", "is_student": true, "address": null}'

# py_obj = json.loads(json_str) # convert json string to python object
# json_str = json.dumps(py_obj)
# print(type(json_str), json_str)
# print(py_obj)

import json

data = {
    "name": "Rishabh",
    "is_student": True,
    "age": 20
} 

with open("data.json", "w") as f:
    json.dump(data, f, indent=4, sort_keys=True) # convert python object to json string and write to file

# with open("data.json", "r") as f:
#     py_obj = json.load(f)
#     print(type(py_obj), py_obj)
