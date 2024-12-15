# Assignment: Python Programming Exercises

# 1. Write a program that takes the user's name and PAN card number as input. Validate the information using `isX` functions and print the details.
name = input("Enter your name: ")
pan = input("Enter your PAN card number: ")

if name.isalpha() and pan.isalnum():
    print(f"Name: {name}")
    print(f"PAN Card Number: {pan}")
else:
    print("Invalid input! Ensure the name contains only letters and the PAN contains only alphanumeric characters.")

# 2. Write a program to generate an Abecedarian series (a series in which elements appear in alphabetical order).
abecedarian_series = [chr(i) for i in range(ord('a'), ord('z')+1)]
print("Abecedarian Series:", abecedarian_series)

# 3. Write a program that counts the occurrences of a character in a string. Do not use built-in functions.
string = input("Enter a string: ")
char = input("Enter a character to count: ")
count = 0
for c in string:
    if c == char:
        count += 1
print(f"The character '{char}' appears {count} times in the string.")

# 4. Write a function that takes a list of words and returns the length of the longest one.
def longest_word_length(words):
    max_length = 0
    for word in words:
        if len(word) > max_length:
            max_length = len(word)
    return max_length

words = input("Enter a list of words (separated by spaces): ").split()
print("Length of the longest word:", longest_word_length(words))

# 5. Write a function to get the first half of a specified string of even length.
def first_half(string):
    if len(string) % 2 == 0:
        return string[:len(string) // 2]
    else:
        return "String length is not even."

string = input("Enter an even-length string: ")
print("First half of the string:", first_half(string))

# 6. Write a program to get a single string from two given strings separated by a space and swap the first two characters of each string.
string1 = input("Enter first string: ")
string2 = input("Enter second string: ")

new_string1 = string2[:2] + string1[2:]
new_string2 = string1[:2] + string2[2:]

result = new_string1 + " " + new_string2
print("Result:", result)

# 7. Write a program to print floating point numbers with no decimal places.
number = float(input("Enter a floating-point number: "))
print("Number with no decimal places:", int(number))
