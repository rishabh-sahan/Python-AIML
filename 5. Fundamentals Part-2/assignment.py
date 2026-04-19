'''
Write a program that takes salary as input. using conditional statements, calculate the final tax rate based on these rules:
If salary < 30,000 -> 5%
If salary is 30,000 - 70,000 -> 15%
If salary > 70,000 -> 25%
'''
# salary = int(input("Enter your salary: "))
# if salary < 30000:
#     tax_rate = 0.05
# elif salary <= 70000:
#     tax_rate = 0.15
# else:
#     tax_rate = 0.25
# final_tax = salary * tax_rate
# print("Tax rate:", tax_rate * 100, "%")
# print("Your final tax is:", final_tax)

'''
Write a function that takes two integers a and b and prints all even numbers between a and b (inclusive).
'''
# def print_even_numbers(a, b):
#     for i in range(a, b + 1):
#         if i % 2 == 0:
#             print(i)
# a = int(input("Enter the first integer: "))
# b = int(input("Enter the second integer: "))
# print_even_numbers(a, b)

'''
Write a function that prints the digits of a number.
For example, if n = 312, there are 3 digits in it: 3, 1, and 2, and we need to print them.
'''
# def print_digits(n):
#     for digit in str(n):
#         print(digit)
# n = int(input("Enter a number: "))
# print_digits(n)

'''
Write a function that returns the number of digits in a number n.
'''
# def count_digits(n):
#     count = 0
#     while n > 0:
#         n //= 10
#         count += 1
#     return count
# n = int(input("Enter a number: "))
# print("Number of digits:", count_digits(n))

'''
write a function to return the sum of digits of n
'''
# def sum_of_digits(n):
#     total = 0
#     while n > 0:
#         total += n % 10
#         n //= 10
#     return total
# n = int(input("Enter a number: "))
# print("Sum of digits:", sum_of_digits(n))

'''
Write a program to print all numbers from 1 to 100 that are divisible by both 3 and 5
'''
# for i in range (1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print(i)

'''
Design a program to continuously input a number n from user & print if it is positive or negative until the user enters “Quit”.
'''
# while True:
#     user_input = input("Enter a number or type 'Quit' to stop: ")
#     if user_input == "Quit" or user_input == "quit":
#         break
#     num = float(user_input)
#     if num > 0:
#         print("Positive number")
#     elif num < 0:
#         print("Negative number")
#     else:
#         print("Zero")

'''
create a simple calculator function that performs operations based on the operation parameter (+, -, *, /).
'''
# def calculator(a, b, operation):
#     if operation == "+":
#         return a + b
#     elif operation == "-":
#         return a - b
#     elif operation == "*":
#         return a * b
#     elif operation == "/":
#         return a / b
#     else:
#         return "Invalid operation"
# a = float(input("Enter the first number: "))
# b = float(input("Enter the second number: "))
# operation = input("Enter the operation (+, -, *, /): ")
# result = calculator(a, b, operation)
# print("Result:", result)

'''
The question asks to write a function is_prime(n) that returns True if the number is prime, otherwise False.
'''
# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True
# num = int(input("Enter a number: "))
# if is_prime(num):
#     print("Prime number")
# else:
#     print("Not a prime number")

'''
Number guessing game: Write a program that generates a random number between 1 and 100 and asks the user to guess it. 
The program should give feedback on whether the guess is too low, too high, or correct. 
The game continues until the user guesses the number correctly.
'''
# import random
# random_number = random.randint(1, 100)
# while True:
#     guess = int(input("Guess the number between 1 and 100: "))
#     if guess < random_number:
#         print("Too low! Try again.")
#     elif guess > random_number:
#         print("Too high! Try again.")
#     else:
#         print("Congratulations! You guessed the number.")
#         break