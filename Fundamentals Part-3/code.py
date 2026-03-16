# Strings
# word = "python"
# print(len(word))

# word1 = "Hello"
# word2 = "World"
# print(word1 + " " + word2) # Concatenation

# word = "python"
# print(word[1]) # Accessing characters
# for ch in word:
#     print(ch) # Iterating through characters

# Slicing
# word = "Rishabh Sahan Jain"
# print(word[8:13]) # Sahan
# print(word[14:]) # Jain
# print(word[:7]) # Rishabh

# Normal Formatting
# a = 5
# b = 10
# sum = a + b
# print("Sum of {} and {} is {}".format(a, b, sum)) # String formatting

# f-Strings
# a = 5
# b = 10
# print(f"Sum of {a} and {b} is {a + b}") # f-String formatting

# marks = [99, 89, 100, 65, 95, 111.11, "abcd"]
# marks[2] = 95 # Modifying elements
# print(marks)
# print(type(marks)) 
# print(len(marks))
# print(marks[2]) # Accessing elements
# print(marks[1:4]) # Slicing elements in list
# print(marks[5:])

# nums = [1, 2, 3, 4]
# nums.append(5) # Adding element to the end of the list
# print(nums)

# nums.insert(2, 2.5) # Inserting element at a specific index
# print(nums)

# nums.insert(4, 10) 
# print(nums)

# nums.sort() # Sorting the list
# print(nums)

# nums.sort(reverse=True) # Sorting in reverse order
# print(nums)

# nums.reverse() # Reversing the list
# print(nums)

# nums = [1, 2, 3, 10, 4]
# for val in nums:
#     print(val) 

# Linear Search
# nums = [1, 2, 3, 10, 4]
# x = 10
# idx = 0
# for val in nums:
#     if val == x:
#         print(f"{x} found at idx = {idx}")
#         break
#     idx += 1

# Tuples
# tup = (1, 2, 3, 4, "abc", 3.14)
# print(tup)
# print(type(tup))
# print(len(tup))
# print(tup[2]) # Accessing elements
# print(tup[0:3]) # Slicing elements in tuple

# tup = (1, 2, 3, 4, 5)
# for val in tup:
#     print(val) # Iterating through tuple

# sum = 0
# for val in tup:
#     sum += val
# print(f"Sum of vals is {sum}")

# Tuples Methods
# tup = (1, 2, 2, 3, 2, 4, 5)
# print(tup.index(2)) # Find the index of the first occurrence of an element
# print(tup.count(2)) # Count the number of occurrences of an element

# Dictionaries
# info = {
#     "name": "Rishabh Jain",
#     "cgpa": 6.0,
#     "skills": ["Python", "Web Dev", "Hacking"],
#     3.14: "PI"
# }
# info["cgpa"] = 7.5 # Modifying values

# print(info)
# print(type(info))
# print(info["name"]) # Accessing values using keys
# print(info[3.14]) # Accessing values using keys
# print(info["cgpa"]) # Accessing values using keys

# Dictionaries Methods
# dict_keys = info.keys() # Get all keys in the dictionary
# print(dict_keys)
# dict_keys = list(info.keys()) 
# print(type(dict_keys)) # Convert dict_keys to a list
# print(info.keys()) # Get all keys in the dictionary
# dict_vals = list(info.values()) 
# print(dict_vals) # Get all values in the dictionary
# print(info.items()) # Get all key-value pairs in the dictionary
# print(info.get("cgpa")) # Get value for a key, returns None if key is not found
# print(info.get("cgpa2")) # Get value for a key, returns None if key is not found
# print("End of code")

# info.update({
#     "city": "Delhi",
#     "country": "India"
# })
# print(info)

# Sets
# set = {1, 2, 2, 2, 3, 4}
# print(set) # Duplicates are removed in sets
# print(type(set))
# print(len(set))
# set.add(5) # Adding element to the set
# print(set)
# set.remove(1) # Removing element from the set
# print(set)
# set.clear() # Removing all elements from the set
# print(set)
# set.pop() # Removing a random element from the set
# print(set)

# s1 = {1, 2, 3, 4, 5}
# s2 = {4, 5, 6, 7, 8}
# # Union of sets
# print(s1.union(s2)) # {1, 2, 3, 4, 5, 6, 7, 8}
# print(s1 | s2) # {1, 2, 3, 4, 5, 6, 7, 8}
# # Intersection of sets
# print(s1.intersection(s2)) # {4, 5}
# print(s1 & s2) # {4, 5}

'''
Practice Problem
Given a list of tuples with info(name, subject):
    * list all unique subjects
    * list students enrolled in english
    * create dictionary (student, set of courses)
'''
# Students = [
#     ("Alice", "Math"),
#     ("Bob", "Science"),
#     ("Alice", "Science"),
#     ("Charlie", "Math"),
#     ("Bob", "Math"),
#     ("Alice", "English"),
#     ("Charlie", "English"),
# ]

# unique_courses = set() 
# courses_set = set()
# for tup in Students:
    # print(tup[0]) # Accessing names
    # print(tup[1]) # Accessing subjects
    # unique_courses.add(tup[1]) # Adding subjects to the set
# print(unique_courses)
# for name, course in Students:
#     print(name, course) # Accessing names

# for name, course in Students:
#     if course == "English":
#         print(name) # List students enrolled in English

# dict = {}
# for name, course in Students:
#     if(dict.get(name) == None):
#         dict.update({name: set()})
#         dict[name].add(course)
#     else:
#         dict[name].add(course)
# print(dict)