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
