# class Student:
#     subject = "Python"
#     college = "Apna College"
#     year = "3rd Year"

# stu1 = Student()
# stu2 = Student()
# print(stu1.subject, stu1.college, stu1.year)
# print(stu2.subject, stu2.college, stu2.year)
# print(type(stu1))

# class Student:
#     def __init__(self): # Default Constructor
#         print("Constructor called")

# class Student:
#     def __init__(self, name, cgpa): # Parameterized Constructor
#         self.name = name
#         self.cgpa = cgpa

#     def get_cgpa(self):
#         return self.cgpa
        
# stu1 = Student("Alice", 9.5)
# stu2 = Student("Bob", 8.7)
# stu3 = Student("Charlie", 9.2)

# print(stu1.name, stu1.cgpa)
# print(stu2.name, stu2.cgpa)
# print(stu3.name, stu3.cgpa)
# print(f"{stu1.name} has cgpa = {stu1.get_cgpa()}")

# class Student:
#     college_name = "Apna College" # Class Variable
#     PI = 3.1

#     def __init__(self, name, cgpa): # Instance Variables
#         self.name = name
#         self.cgpa = cgpa
#         self.PI = 3.14 # Local Variable

# stu1 = Student("Alice", 9.5)
# print(stu1.name)
# print(stu1.cgpa)
# print(stu1.college_name)
# print(stu1.PI)
# print(Student.PI)

# class Laptop:
#     storage_type = "SSD" # Class Variable

#     def __init__(self, RAM, storage):
#         self.RAM = RAM # Instance Variable
#         self.storage = storage # Instance Variable

#     @classmethod # Decorator
#     def get_storage_type(cls): # Class Method
#         print(f"storage type = {cls.storage_type}")
    
#     def get_info(self): # Instance Method
#         print(f"laptop has {self.RAM} RAM & {self.storage} {self.storage_type}")

#     @staticmethod # Decorator
#     def calc_discount(price, discount):
#         final_price = price - (discount * price / 100)
#         print(f" discounted price = {final_price}")

# l1 = Laptop("16GB", "512GB") 
# l2 = Laptop("8GB", "256GB")

# l1.calc_discount(40_000, 10)

# l1.get_info()
# l2.get_info()

# Laptop.get_storage_type() # Class Method can be called using class name
# l1.get_storage_type() # Class Method can also be called using object but it will not have access to instance variables, it will only have access to class variables

'''
Product Store
Design & create an online store for products (name, price).
Track total products being created.
Create a static method to calculate discount on each product based on a % parameter.
'''

# class Product:
#     count = 0

#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#         Product.count += 1

#     def get_info(self): # Instance Method
#         print(f"price of {self.name} is Rs. {self.price}")

#     @classmethod
#     def get_count(cls):
#         print(f"total products in store = {cls.count}")

#     @staticmethod
#     def calc_discount(price, discount):
#         print(f"discounted price = Rs. {price - (price * discount / 100)}")

# p1 = Product("Laptop", 40_000)
# p2 = Product("Smartphone", 20_000)
# p3 = Product("Headphones", 5_000)

# p1.get_info()
# Product.get_count()
# p1.calc_discount(40_000, 10) 
# p2.calc_discount(p2.price, 15)

# OOP Pillars
# Encapsulation

# class BankAccount:
#     def __init__(self, name, balance):
#         self.name = name # Public Attribute
#         self.__balance = balance # Private Attribute

#     def get_balance(self):
#         return self.__balance 

#     def set_balance(self, newBalance):
#         self.__balance = newBalance

# acc1 = BankAccount("Alice", 100_000)
# acc1.set_balance(120_000)
# print(acc1.name, acc1.get_balance()) # Accessing private attribute using getter method
# print(acc1.name, acc1._BankAccount__balance) # Accessing private attribute using name mangling (not recommended)

# Inheritance

# class Employee:
#     start_time = "10am"
#     end_time = "6pm"

    # def change_time(self, new_end_time):
    #     self.end_time = new_end_time

# class Teacher(Employee):
#     def __init__(self, subject):
#         self.subject = subject

# class AdminStaff(Employee):
#     def __init__(self, role):
#         self.role = role

# class Accountant(AdminStaff):
#     def __init__(self, salary, role):
#         super().__init__(role) # Call the constructor of AdminStaff to initialize role
#         self.salary = salary

# t1 = Teacher("Math")
# t1.change_time("5pm")

# print(t1.subject, t1.start_time, t1.end_time)

# staff1 = AdminStaff("Manager")
# print(staff1.role, staff1.start_time, staff1.end_time)

# acc1 = Accountant(50_000, "CA")
# print(acc1.role, acc1.salary, acc1.start_time, acc1.end_time)

# class Teacher:
#     def __init__(self, salary):
#         self.salary = salary

# class Student:
#     def __init__(self, cgpa):
#         self.cgpa = cgpa
    
# class TA(Teacher, Student):
#     def __init__(self, salary, cgpa, name):
#         super().__init__(salary)
#         Student.__init__(self, cgpa)
#         self.name = name

# ta1 = TA(30_000, 9.5, "Alice")
# print(ta1.name, ta1.salary, ta1.cgpa)

# from abc import ABC, abstractmethod
# class Animal(ABC):
#     @abstractmethod
#     def make_sound(self):
#         pass

# class Lion(Animal):
#     def make_sound(self):
#         print("Roar")

# class Cow(Animal):
#     def make_sound(self):
#         print("Moo!!")

# lion = Lion()
# lion.make_sound()

# cow = Cow()
# cow.make_sound()

# class Employee:
#     def get_designation(self):
#         print("designation = Employee")

# class Teacher(Employee):
#     def get_designation(self):
#         print("designation = Teacher")

# t1 = Teacher()
# t1.get_designation()

# class Teacher:
#     def get_designation(self):
#         print("designation = Teacher")

# class Accountant:
#     def get_designation(self):
#         print("designation = Accountant")

# t1 = Teacher()
# t1.get_designation()
# a1 = Accountant()
# a1.get_designation()