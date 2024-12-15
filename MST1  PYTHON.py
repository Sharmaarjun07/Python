x=input("Enter the value= ")
if x.isdigit():
     print("it is an integer")
elif x.isalpha():
    print("it is an character")
else:
    print("it is an special character")
    
    
y=input("Enter the value= ")  
if 'A'<=y<='Z':
    print("UPPER CASE")
else:
    print("LOWER CASE")  
    
list1=[1,2,3,4,5]
sum1=0
for i in range (len(list1)):
    sum1=(sum1)+(list1[i])
print(sum1)


#lambda functions:they dont need to  be declared
#function=lambda argument:expression
add=lambda num:num+4
print(add(6))


a=lambda x,y:(x**y)
print(a(2,3))

#RECURSION
#split the fncn in two parts
#1.BASE CASE
def factorial(n):
    if n==0:
        return 1
    
    else:  
        return n*factorial(n-1)
        
print(factorial(4))




#FABBONACI SERIES

def fabbonaci(n):

    if n<=0:
        print("fabbonaci cannot be formed")
    else:
        a=0
        b=1
        for i in range (n):
          print(a)
          sum1=a+b 
          a=b
          b=sum1
        

fabbonaci(10)
print("________________________________________________________________________")
#ASSIGNMENTS1

#1 Calculate Area of Circle 
a=int(input("Enter the radius="))
area1=3.14*a*a
print("AREA=",area1)

#2 WAP to print  ones digit of number
a=int(input("Enter the number"))
c=a%10
print("ones digit no.",c)

#3 WAP to find avg of two numbers and there deviation too
Num1=int(input("Enter a number 1:"))
Num2=int(input("Enter a number 2: "))
Avg=(Num1+ Num2)/2
Deviation1=Num1-Avg
Deviation2=Num2-Avg
print("The deviation between Number1 and Avg is",Deviation1)
print("The deviation between Number2 and Avg is",Deviation2)

#4 WAP to covert floating number its corresponding integer 
Floating_Number=float(input("Enter the value"))
integer_value=int(Floating_Number)
print("The value after conversion from float to integer is ",integer_value)

#5 WAP to convert Fahrenheit to Celsius 
Fahrenheit=int(input("Enter the number"))
Celsius=(5/9)*(Fahrenheit-32)
print("Fahrenheit value is",Fahrenheit, "and in Celsius its value is ",Celsius)


#ASSIGNMENT2
#Write a program to calculate the distance between two points.
import math

def calculate_distance(x1, y1, x2, y2):
    """Calculate the distance between two points (x1, y1) and (x2, y2)."""
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance

if __name__ == "__main__":
    # Input coordinates for the first point
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))

    # Input coordinates for the second point
    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))

    # Calculate the distance
    distance = calculate_distance(x1, y1, x2, y2)

    # Output the result
    print(f"The distance between the points ({x1}, {y1}) and ({x2}, {y2}) is: {distance:.2f}")

#Write a program to calculate the area of a triangle using Herons formula

import math

def calculate_area(a, b, c):
    """Calculate the area of a triangle using Heron's formula."""
    # Calculate the semi-perimeter
    s = (a + b + c) / 2
    # Calculate the area using Heron's formula
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

if __name__ == "__main__":
    # Input lengths of the sides of the triangle
    a = float(input("Enter the length of side a: "))
    b = float(input("Enter the length of side b: "))
    c = float(input("Enter the length of side c: "))

    # Check if the sides can form a triangle
    if a + b > c and a + c > b and b + c > a:
        # Calculate the area
        area = calculate_area(a, b, c)
        # Output the result
        print(f"The area of the triangle with sides {a}, {b}, and {c} is: {area:.2f}")
    else:
        print("The lengths provided cannot form a triangle.")

#Write a program to calculate the bill amount for an item given its quantity sold,
#value, discount, and tax. Given a string s = "1234" and an integer n = 5678,
#concatenate them as a single string and then convert the result back to an integer.
#What is the final integer value?

def calculate_bill(quantity, value, discount, tax):
    """Calculate the total bill amount."""
    # Calculate the total value
    total_value = quantity * value
    
    # Apply discount
    discount_amount = (discount / 100) * total_value
    discounted_value = total_value - discount_amount
    
    # Apply tax
    tax_amount = (tax / 100) * discounted_value
    total_bill = discounted_value + tax_amount
    
    return total_bill

if __name__ == "__main__":
    # Input details from the user
    quantity = int(input("Enter the quantity sold: "))
    value = float(input("Enter the value of the item: "))
    discount = float(input("Enter the discount percentage: "))
    tax = float(input("Enter the tax percentage: "))

    # Calculate the bill amount
    bill_amount = calculate_bill(quantity, value, discount, tax)

    # Output the result
    print(f"The total bill amount is: ${bill_amount:.2f}")

# Given values
s = "1234"
n = 5678

# Concatenate the string and the integer (convert integer to string first)
result_string = s + str(n)

# Convert the concatenated result back to an integer
final_integer_value = int(result_string)

# Output the final integer value
print(f"The final integer value is: {final_integer_value}")

#4. Given two variables, a = 7 and b = 3, write a Python code snippet to
#swap their values without using a temporary variable. What will be the
#values of a and b after the swap?
# Given values
a = 7
b = 3

# Swapping values without a temporary variable
a, b = b, a

# Output the results
print(f"After swapping: a = {a}, b = {b}")

#5. Given a list of numbers = [10, 20, 30, 40, 50], write a Python code
#snippet to calculate the average of these numbers using arithmetic
#operators.

# Given list of numbers
numbers = [10, 20, 30, 40, 50]

# Calculate the sum of the numbers
total_sum = sum(numbers)

# Calculate the number of elements
count = len(numbers)

# Calculate the average
average = total_sum /count

# Output the result
print(f"The average of the numbers is: {average}")


#6. Write a simple basic calculator program in python.
# Given list of numbers
numbers = [10, 20, 30, 40, 50]

# Calculate the sum of the numbers
total_sum = sum(numbers)

# Calculate the number of elements
count = len(numbers)

# Calculate the average
average = total_sum / count

# Output the result
print(f"The average of the numbers is: {average}")



#ASSIGNMENT3

#Q1. WAP that finds greatest of three numbers using functions. Pass the numbers as arguments..
def find_greatest(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

if __name__ == "__main__":
    # Pass the numbers as arguments
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    number3 = float(input("Enter the third number: "))

    greatest = find_greatest(number1, number2, number3)
    print(f"The greatest number among {number1}, {number2}, and {number3} is: {greatest}")

#Q2. Write a program to implement these formulae of permutation and combinations.
#Number of permutations of n objects taken r at a time :p(n,r)=n!/(n-r)! . Number of combinations of n objects 
#taken r at a time is:c(n,r)=n!/(r!*(n-r)!)=p(n,r)/r!
def factorial(n):
    """Calculate the factorial of n recursively."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def permutations(n, r):
    """Calculate the number of permutations of n objects taken r at a time."""
    return factorial(n) // factorial(n - r)

def combinations(n, r):
    """Calculate the number of combinations of n objects taken r at a time."""
    return permutations(n, r) // factorial(r)

if __name__ == "__main__":
    # Input values for n and r
    n = int(input("Enter the total number of objects (n): "))
    r = int(input("Enter the number of objects to choose (r): "))
    
    if r > n:
        print("r cannot be greater than n.")
    else:
        p = permutations(n, r)
        c = combinations(n, r)
        
        print(f"Number of permutations of {n} objects taken {r} at a time: P({n}, {r}) = {p}")
        print(f"Number of combinations of {n} objects taken {r} at a time: C({n}, {r}) = {c}")


#Q3. Write a function cubesum() that accepts an integer and returns the sum of the cubes of  individual 
#digits of that number. Use this function to make functions PrintArmstrong() and isArmstrong() to print 
#Armstrong numbers and to find whether is an Armstrong number.


def cubesum(n):
    """Calculate the sum of the cubes of the individual digits of n."""
    total = 0
    while n > 0:
        digit = n % 10  # Get the last digit
        total += digit ** 3  # Add the cube of the digit
        n //= 10  # Remove the last digit
    return total

def isArmstrong(num):
    """Check if a number is an Armstrong number."""
    return cubesum(num) == num

def PrintArmstrong(limit):
    """Print all Armstrong numbers up to a given limit."""
    print(f"Armstrong numbers up to {limit}:")
    for num in range(limit + 1):
        if isArmstrong(num):
            print(num, end=' ')
    print()  # For a new line

if __name__ == "__main__":
    # Input limit from user
    limit = int(input("Enter the limit to find Armstrong numbers: "))
    PrintArmstrong(limit)


#Q4. Write a Python function to create and print a list where the values are the squares of
#numbers between 1 and 30 (both included).

def squares_list():
    """Create and print a list of squares of numbers between 1 and 30."""
    squares = [i**2 for i in range(1, 31)]  # List comprehension to create the list of squares
    print(squares)

if __name__ == "__main__":
    squares_list()


#Q5. Given a string s = “1234” and an integer n = 5678, concatenate them as a single string
#and then convert the result back to an integer. What is the final integer value?

s = "1234"
n = 5678

# Step 1: Convert the integer to a string
n_str = str(n)

# Step 2: Concatenate the two strings
result_str = s + n_str

# Step 3: Convert the concatenated string back to an integer
final_integer = int(result_str)

print(final_integer)  # Output the final integer value



#Q6. Write a Python program that repeatedly asks the user to enter a positive integer. If the
#user enters a negative number or zero, the program should ask again until a positive
#integer is entered.
def get_positive_integer():
    """Prompt the user to enter a positive integer until a valid input is received."""
    while True:
        try:
            number = int(input("Please enter a positive integer: "))
            if number > 0:
                return number
            else:
                print("That's not a positive integer. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    positive_integer = get_positive_integer()
    print(f"You entered a positive integer: {positive_integer}")


#PYQ
## MID SEM

# Q1: Write a function in Python to check duplicate letters. It must accept a string, i.e., a sentence.
# The function should return True if the sentence has any word with duplicate letters, else return False.

def has_duplicate_letters(sentence):
    # Split the sentence into words
    words = sentence.split()
    
    # Loop through each word
    for word in words:
        # Use a set to track characters in the word
        seen = set()
        for char in word:
            if char in seen:
                return True  # Duplicate letter found in the word
            seen.add(char)
    
    return False  # No duplicate letters in any word

sentence = "This is a test"
print(has_duplicate_letters(sentence))  # Output: True

# Q2: Write a function in Python to parse a string such that it accepts a parameter- an encoded string.
# This encoded string will contain a first name, last name, and an id. You can separate the values 
# in the string by any number of zeros. The id will not contain any zeros.

def parse_encoded_string(encoded_str):
    # Split the string by '0's and remove empty strings from the result
    parts = [part for part in encoded_str.split('0') if part]
    
    # Assign the first, second, and third parts to first_name, last_name, and id respectively
    if len(parts) == 3:
        first_name, last_name, id_val = parts
        return {"first_name": first_name, "last_name": last_name, "id": id_val}
    else:
        raise ValueError("Encoded string does not contain valid first name, last name, and id format")

encoded_str = "John000Doe000123"
result = parse_encoded_string(encoded_str)
print(result)  # Output: {'first_name': 'John', 'last_name': 'Doe', 'id': '123'}

# Q3: Develop a function that takes a list and checks whether all elements in the list are the same.

def all_equal(lst):
    # Check if all elements in the list are the same by comparing them to the first element
    return all(element == lst[0] for element in lst) if lst else True

print(all_equal([1, 1, 1]))  # Output: True
print(all_equal([1, 2, 1]))  # Output: False
print(all_equal([]))         # Output: True

# Q4: Write a Python program that accepts a word from the user and reverses it.

# Accept input from the user
word = input("Enter a word: ")

# Reverse the word using slicing
reversed_word = word[::-1]

# Display the reversed word
print("Reversed word:", reversed_word)

# Q5: Write a function in Python that should intake two integer values and return a True or False 
# based upon whether these integers are Anagram or not.

def are_anagrams(num1, num2):
    # Convert both numbers to strings
    str_num1 = str(num1)
    str_num2 = str(num2)
    
    # Sort the digits of both numbers and compare
    return sorted(str_num1) == sorted(str_num2)

print(are_anagrams(123, 321))  # Output: True
print(are_anagrams(123, 456))  # Output: False
print(are_anagrams(1122, 2211))  # Output: True

# Q6: WAP in Python to print patterns

# 1.
n=5
for i in range(1, n+1):
    print(' ' * (n-i) + '* ' * i)

# 2.
n = 5
for i in range(1, n+1):
    print('* ' * i)

# Q7: You have three lists of words. Create all possible combinations of sentences by taking one element from each list.

import itertools

list1 = ['I', 'You', 'We']
list2 = ['like', 'love']
list3 = ['Python', 'Java']

# Create all combinations using itertools.product
combinations = itertools.product(list1, list2, list3)

# Convert the tuple combinations into sentences
sentences = [' '.join(comb) for comb in combinations]

# Display all combinations
for sentence in sentences:
    print(sentence)

# Q8: Write a Python program to convert more than one list to a nested dictionary.

codes = ['S001', 'S002', 'S003', 'S004']
names = ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
scores = [85, 98, 89, 92]

# Create the nested dictionary without list concatenation
nested_dict = []
for i in range(len(codes)):
    nested_dict.append({codes[i]: {names[i]: scores[i]}})

# Print the result
print(nested_dict)

# Q9: Write a Python program to get a string made of the first 2 and last 2 characters of a given string.

def string_ends(string):
    # Check if the string length is less than 2
    if len(string) < 2:
        return ''
    
    # Return a string made of the first 2 and last 2 characters
    return string[:2] + string[-2:]

# Example Usage
print(string_ends('Python'))  # Output: 'Pyon'
print(string_ends('Py'))      # Output: 'PyPy'
print(string_ends('P'))       # Output: ''
