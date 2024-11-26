# # Uppgifter OOP
# # 1. Skapa en klass
# class Book:
#     def __init__(self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year = year

#     def get_info(self):
#         return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"
    
#     def is_classic(self):
#         currentYear = 2024
#         calculate = currentYear - self.year 
#         return calculate > 50

# bok1 = Book("Jag är Zlatan Ibramhimovich", "David Lagercrantz", 1960)
# print(bok1.get_info())
# #2. Lägg till en metod
# print(bok1.is_classic())

# class Student:
#     def __init__(self, name, age, grades):
#         self.name : str = name
#         self.age : int = age
#         self.grades : list = grades

#     def average_grade(self):
#         return f"Medelbetyg: {sum(self.grades) / len(self.grades)}"

# student1 = Student("Hilmer", 21, [5, 2, 1, 4])
# student2 = Student("Jakob", 21, [4, 2, 10, 4])
# student3 = Student("Samuel", 21, [5, 7, 1, 4])

# print(student1.average_grade())
# print(student2.average_grade())
# print(student3.average_grade())

# # 4. Inkapsling
# class BankAccount:
#     def __init__(self):
#         self.__balance = 0

#     def deposit(self, amount):
#         self.__balance += amount
    
#     def withdraw(self, amount):
#         self.__balance -= amount

#     def get_balance(self):
#         return self.__balance    


    
# Bank1 = BankAccount()
# Bank1.deposit(100)
# print(Bank1.get_balance())
# Bank1.withdraw(50)
# print(Bank1.get_balance())

# #5. Arv
# # 6. Skriv över metoder (Tillägg)
# class Animal:
#     def __init__(self, name):
#         self.name : str = name
    
#     def make_sound(self):
#         return "Some sound"
    
#     def describe(self):
#         return f"This is an animal named {self.name}"

# class Dog(Animal):
#     def make_sound(self):
#         return "Wooof!!"
    
#     def describe(self):
#         return f"This is an dog named {self.name}"
    
# class Cat(Animal):
#     def make_sound(self):
#         return "Meooow!!"
    
#     def describe(self):
#         return f"This is an cat named {self.name}"
    
# Djur1 = Dog('Gusto')
# print(Djur1.make_sound())
# print(Djur1.describe())

# Djur2 = Cat('Ribla')
# print(Djur2.make_sound())
# print(Djur2.describe())

# #7. Polymorfism
# def animal_sounds(animals):
#     for animal in animals:
#         print(animal.make_sound())

# # Test
# Djur1 = Dog("Gusto")
# Djur2 = Cat("Ribla")
# animal_sounds([Djur1, Djur2])

# #8. En avancerad metod
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         area = self.width * self.height
#         return area
    
#     def perimeter(self):
#         omkrets = (self.width * 2) + (self.height * 2)
#         return omkrets

# calculate = Rectangle(5, 10)
# print(calculate.area())
# print(calculate.perimeter())

# # 10. Hantera flera klasser
# class Address:
#     def __init__(self, street, city):
#         self.street = street
#         self.city = city

# class Person:
#     def __init__(self, name, age, address):
#         self.name = name
#         self.age = age
#         self.address = address

# # Test
# address = Address("Baker Street", "London")
# person = Person("Sherlock Holmes", 40, address)

# print(person.name)  # Output: Sherlock Holmes
# print(person.age)   # Output: 40
# print(person.address.street)  # Output: Baker Street
# print(person.address.city)    # Output: London

# OOP - Python Övningar
# 1. Kunddatabas

# class Customer:
#     def __init__(self, name, email, phone, address):
#         self.name = name
#         self.email = email
#         self.phone = phone
#         self.address = address


# class CustomerDatabase:
#     def __init__(self):
#         self.customers = []

#     def add_customer(self, customer):
#         self.customers.append(customer)

#     def update_customer(self, email, new_data):
#         for customer in self.customers:
#             if customer.email == email:
#                 customer.name = new_data.get("name", customer.name)
#                 customer.phone = new_data.get("phone", customer.phone)
#                 customer.address = new_data.get("address", customer.address)
#                 return "Customer updated."
#         return "Customer not found."

#     def list_customers(self):
#         return [f"{cust.name}, {cust.email}" for cust in self.customers]

#     def find_customer(self, search_email):
#         for customer in self.customers:
#             if customer.email == search_email:
#                 return vars(customer)
#         return "Customer not found."


# # Exempelanvändning
# db = CustomerDatabase()
# c1 = Customer("Anna Andersson", "anna@example.com", "123456789", "Stockholm")
# c2 = Customer("Lars Larsson", "lars@example.com", "987654321", "Malmö")

# db.add_customer(c1)
# db.add_customer(c2)
# print(db.list_customers())
# print(db.find_customer("anna@example.com"))
# print(db.update_customer("anna@example.com", {"phone": "555555555"}))

# #2. Enkelt CRM-system
# class Customer:
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#         self.interactions = []

#     def add_interaction(self, interaction):
#         self.interactions.append(interaction)


# class CRMSystem:
#     def __init__(self):
#         self.customers = []

#     def add_customer(self, customer):
#         self.customers.append(customer)

#     def record_interaction(self, email, interaction):
#         for customer in self.customers:
#             if customer.email == email:
#                 customer.add_interaction(interaction)
#                 return "Interaction added."
#         return "Customer not found."

#     def view_interactions(self, email):
#         for customer in self.customers:
#             if customer.email == email:
#                 return customer.interactions
#         return "Customer not found."


# # Exempelanvändning
# crm = CRMSystem()
# c1 = Customer("Sara Svensson", "sara@example.com")
# crm.add_customer(c1)

# crm.record_interaction("sara@example.com", "E-post om uppdaterade villkor.")
# print(crm.view_interactions("sara@example.com"))


# #10. Kundsupportsystem
# class SupportTicket:
#     def __init__(self, errand, customer, problem, status):
#         self.errand = errand
#         self.customer = customer
#         self.problem = problem
#         self.status = status
#         print(self.errand, self.customer, self.problem, self.status)

# class SupportManager:
#     def __init__(self):
#         self.tickets = []

#     def add_customer(self, customer):
#         self.tickets.append(customer)
#         for ticket in self.tickets:
#             print(ticket)
#             print(self.tickets)


# s1 = SupportTicket('01239', 'Hilmer', 'Forgot PW', 'Open')
# manager = SupportManager()
# manager.add_customer(s1)