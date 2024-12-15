#ASSIGNMENT 6
#1. Write a program that has a class Fraction with attributes numerator and denominator. Enter
#the values of the attributes and print the fraction in simplified form.
from math import gcd

class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")
        self.numerator = numerator
        self.denominator = denominator
        self.simplify()
    
    def simplify(self):
        """Simplifies the fraction using the GCD of numerator and denominator."""
        common_divisor = gcd(self.numerator, self.denominator)
        self.numerator //= common_divisor
        self.denominator //= common_divisor

    def __str__(self):
        """Returns the fraction in 'numerator/denominator' format."""
        return f"{self.numerator}/{self.denominator}"

# Example Usage
try:
    num = int(input("Enter numerator: "))
    den = int(input("Enter denominator: "))
    fraction = Fraction(num, den)
    print("Simplified Fraction:", fraction)
except ValueError as e:
    print("Error:", e)



#2. Write a program that has a class store which keeps record of code and price of each product.
#Display a menu of all products to the user and prompt him to enter the quantity of each
#item required. Generate a bill and display the total amount.
class Store:
    def __init__(self):
        self.products = {"101": {"name": "Apple", "price": 10},
                         "102": {"name": "Banana", "price": 5},
                         "103": {"name": "Orange", "price": 8}}
        self.cart = {}

    def display_menu(self):
        print("Product Menu:")
        for code, details in self.products.items():
            print(f"Code: {code}, Name: {details['name']}, Price: {details['price']}")

    def add_to_cart(self, code, quantity):
        if code in self.products:
            self.cart[code] = self.cart.get(code, 0) + quantity
        else:
            print("Invalid product code!")

    def generate_bill(self):
        total = 0
        print("\nBill Details:")
        for code, quantity in self.cart.items():
            product = self.products[code]
            cost = product["price"] * quantity
            total += cost
            print(f"{product['name']} x {quantity} = {cost}")
        print(f"Total Amount: {total}")

# Example Usage
store = Store()
store.display_menu()
while True:
    code = input("Enter product code (or 'done' to finish): ")
    if code.lower() == "done":
        break
    quantity = int(input("Enter quantity: "))
    store.add_to_cart(code, quantity)
store.generate_bill()



#3. Write a class that stores a string and all its status details such as number of uppercase
#characters, vowels, consonants, spaces etc.


class StringStatus:
    def __init__(self, input_string):
        self.input_string = input_string

    def analyze(self):
        self.uppercase = sum(1 for c in self.input_string if c.isupper())
        self.vowels = sum(1 for c in self.input_string.lower() if c in "aeiou")
        self.consonants = sum(1 for c in self.input_string.lower() if c.isalpha() and c not in "aeiou")
        self.spaces = sum(1 for c in self.input_string if c.isspace())

    def display_status(self):
        print(f"Uppercase: {self.uppercase}, Vowels: {self.vowels}, Consonants: {self.consonants}, Spaces: {self.spaces}")

# Example Usage
input_str = input("Enter a string: ")
status = StringStatus(input_str)
status.analyze()
status.display_status()

#4. Write a program that has a class person. Inherit a class Faculty from person which also has
#class Publications.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Faculty(Person):
    def __init__(self, name, age, department):
        super().__init__(name, age)
        self.department = department

class Publications(Faculty):
    def __init__(self, name, age, department, publications):
        super().__init__(name, age, department)
        self.publications = publications

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Department: {self.department}")
        print("Publications:", ", ".join(self.publications))

# Example Usage
faculty = Publications("Dr. Smith", 45, "Computer Science", ["AI Research", "Machine Learning"])
faculty.display()


#5. Write a program that overloads the + operator so that it can add a specified number of days
#to a given date.

import datetime

class Date:
    def __init__(self, day, month, year):
        self.date = datetime.date(year, month, day)

    def __add__(self, days):
        new_date = self.date + datetime.timedelta(days=days)
        return Date(new_date.day, new_date.month, new_date.year)

    def __str__(self):
        return self.date.strftime("%d-%m-%Y")

# Example Usage
date = Date(28, 2, 2024)
new_date = date + 5
print(f"Original Date: {date}")
print(f"New Date: {new_date}")


#6. Write a program to overload -= operator to subtract two Distance objects


class Distance:
    def __init__(self, meters):
        self.meters = meters

    def __isub__(self, other):
        if isinstance(other, Distance):
            self.meters -= other.meters
        return self

    def __str__(self):
        return f"{self.meters} meters"

# Example Usage
dist1 = Distance(150)
dist2 = Distance(50)
print(f"Initial Distance 1: {dist1}")
dist1 -= dist2
print(f"Distance after subtraction: {dist1}")
