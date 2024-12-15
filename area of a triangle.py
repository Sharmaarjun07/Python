#Write a program to calculate the area of a triangle using Heron's formula
import math

def calculate_area(a, b, c):
    # Calculate the semi-perimeter
    s = (a + b + c) / 2
    
    # Calculate the area using Heron's formula
    A = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return A

def main():
    # Input lengths of the sides of the triangle
    a = float(input("Enter length of side a: "))
    b = float(input("Enter length of side b: "))
    c = float(input("Enter length of side c: "))
    
    # Check if the sides form a valid triangle
    if a + b > c and a + c > b and b + c > a:
        # Calculate area
        area = calculate_area(a, b, c)
        print(f"The area of the triangle with sides {a}, {b}, and {c} is {area:.2f}")
    else:
        print("The provided sides do not form a valid triangle.")

main()

