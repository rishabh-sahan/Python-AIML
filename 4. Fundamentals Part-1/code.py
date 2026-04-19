# print("Hello, World!");
# print("Welcome to coding!");

# print("Hello, World!", "Welcome to coding!");

# print("Hello, \nWorld!", "Welcome to coding!");

# Identifiers
# name = "Rishabh"
# _name = "Jain"
# age = 20
# PI = 3.14
# Bool = True
# NoneType = None

# print(name, age, PI)
# print("My Name is:", name)
# print("My Age is:", age+1) # we can also do operations in print statement
# print("My Name is: ", name, _name) # we can also print multiple variables in a single print statement

# Data Types
# print(type(name)) # str
# print(type(age)) # int 
# print(type(PI)) # float
# print(type(Bool)) # bool
# print(type(NoneType)) # NoneType

'''
This is a 
multi-line 
comment
'''

#Style Guide
# tot_price = 100 # snake_case -> preferred for variable and function names
# totPrice = 100 # camelCase
# TotPrice = 100 # PascalCase

# WAP to calculate sum of two numbers
# a = 5
# b = 10
# sum = a + b
# print(sum)

# Arithmetic Operators
# a = 10
# b = 5
# print(a+b) # Addition
# print(a-b) # Subtraction
# print(a*b) # Multiplication
# print(a/b) # Division
# print(a%b) # Modulus
# print(a**b) # Exponentiation

# Relational or Comparison Operators
# a = 10
# b = 5
# print(a == b) # Equal to
# print(a != b) # Not equal to
# print(a > b) # Greater than
# print(a < b) # Less than
# print(a >= b) # Greater than or equal to
# print(a <= b) # Less than or equal to

# Assignment Operators
# a = 10
# a = a + 5 #15 # a = 10 + 5 -> 15
# a += 5 # a = a + 5 -> 20 # a = 15 + 5 -> 20
# a -= 5 # a = a - 5 -> 15 # a = 20 - 5 -> 15
# a *= 5 # a = a * 5 -> 75 # a = 15 * 5 -> 75
# a /= 5 # a = a / 5 -> 15.0 # a = 75 / 5 -> 15.0
# a %= 5 # a = a % 5 -> 0.0 # a = 15.0 % 5 -> 0.0
# a **= 5 # a = a ** 5 -> 0.0 # a = 0.0 ** 5 -> 0.0
# print(a)

# Logical Operators
# Not Operator
# var = False
# print(not var) # True
# print(not (5>8)) # True

# And Operator
# print((5>3) and (3>2)) # True and True -> True
# print((5>3) and (3>8)) # True and False -> False

# OR Operator
# print((5>3) or (3>2)) # True or True -> True
# print((5>3) or (3>8)) # True or False -> True
# print((5>13) or (3>8)) # False or False -> False

# x = 3
# x += 5
# print(x) # 8

# Type Conversion
# a = 10
# b = 5
# print(type(a/b)) # float

# ans = 5 + 10.0
# print(type(ans)) # float

# Type Casting
# ans = int(5 + 10.0)
# print(type(ans))

# val = int("123")
# print(type(val)) # int

'''
in boolean False is considered as 0
and True is considered as everything other than 0
'''

# val = bool(0)
# print(val, type(val))

# val = bool(10)
# print(val, type(val))

# val = bool(-10)
# print(val, type(val))

# ans1 = int(5 + 10.0) # Casting
# ans2 = 5 + 10.0 # Conversion
# print(ans1, type(ans1)) 
# print(ans2, type(ans2))

# a = input("Enter the value of a: ") # input() function is used to take input from the user
# print(a)
# username = input("Enter your name: ")
# print("Welcome", username)

# a = int(input("Enter the value of a: "))
# b = int(input("Enter the value of b: "))
# sum = a + b
# print("The sum of a and b is:", sum)

# a = float(input("Enter the value of a: "))
# b = float(input("Enter the value of b: "))
# sum = a + b
# print("The sum of a and b is:", sum)
# avg = sum / 2
# print("The average of a and b is:", avg)