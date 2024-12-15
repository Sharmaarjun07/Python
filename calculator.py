#Write a simple basic calculator program in python
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

def main():
    print("Simple Basic Calculator")
    # Get user input for numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    # Get user input for operation
    choice = input("Enter choice (1/2/3/4): ")

   

    # Perform the operation based on user choice
    if choice == '1':
        print(f"The result of {num1} + {num2} is {add(num1, num2)}")
    elif choice == '2':
        print(f"The result of {num1} - {num2} is {subtract(num1, num2)}")
    elif choice == '3':
        print(f"The result of {num1} * {num2} is {multiply(num1, num2)}")
    elif choice == '4':
        print(f"The result of {num1} / {num2} is {divide(num1, num2)}")
    else:
        print("Invalid input! Please choose a valid operation.")


main()
