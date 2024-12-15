# Question 1: Write a program that fetches data from a specific URL and prints it on the screen.
import requests

url = "https://example.com"  # Replace with the desired URL
try:
    response = requests.get(url)
    response.raise_for_status()  # Raises an error for HTTP errors
    print("Data fetched from URL:")
    print(response.text)
except requests.exceptions.RequestException as e:
    print(f"Failed to fetch data. Error: {e}")

# Question 2: Write a program that computes the total size of all the files in your current directory folder.
import os

total_size = 0
for file in os.listdir('.'):
    if os.path.isfile(file):
        total_size += os.path.getsize(file)

print(f"Total size of all files in the current directory: {total_size} bytes")

# Question 3: Write a program that reads a file line by line and copies each line to another file with line numbers specified at the beginning of the line
input_file = "input.txt"
output_file = "output.txt"

try:
    with open(input_file, "r") as infile, open(output_file, "w") as outfile:
        for line_num, line in enumerate(infile, start=1):
            outfile.write(f"{line_num}: {line}")
    print(f"File copied to {output_file} with line numbers.")
except FileNotFoundError:
    print(f"Error: {input_file} not found.")
except IOError as e:
    print(f"Error reading/writing file: {e}")

# Question 4: Write a program that counts the number of tabs, spaces, and newline characters in a file
file_name = "example.txt"

try:
    tab_count = space_count = newline_count = 0

    with open(file_name, "r") as file:
        for line in file:
            tab_count += line.count('\t')
            space_count += line.count(' ')
            newline_count += line.count('\n')

    print(f"Tabs: {tab_count}, Spaces: {space_count}, Newlines: {newline_count}")
except FileNotFoundError:
    print(f"Error: {file_name} not found.")
except IOError as e:
    print(f"Error reading file: {e}")

# Question 5: Write a program that reads data from a file and calculates the percentage of vowels and consonants in the file.
file_name = "example.txt"

try:
    vowel_count = consonant_count = total_characters = 0
    vowels = "aeiouAEIOU"

    with open(file_name, "r") as file:
        for char in file.read():
            if char.isalpha():
                total_characters += 1
                if char in vowels:
                    vowel_count += 1
                else:
                    consonant_count += 1

    if total_characters > 0:
        print(f"Vowel Percentage: {(vowel_count / total_characters) * 100:.2f}%")
        print(f"Consonant Percentage: {(consonant_count / total_characters) * 100:.2f}%")
    else:
        print("No alphabetic characters found in the file.")
except FileNotFoundError:
    print(f"Error: {file_name} not found.")
except IOError as e:
    print(f"Error reading file: {e}")

# Question 6: What are the different access modes in which you can open a file?
# Answer:
# The different access modes for opening a file are:
# 'r': Open for reading (default).
# 'w': Open for writing, truncating the file first.
# 'x': Open for exclusive creation; fails if the file already exists.
# 'a': Open for writing, appending to the end of the file if it exists.
# 'b': Binary mode.
# 't': Text mode (default).
# '+': Open for updating (reading and writing).

# Question 7: Write a program that writes data to a file so that each character after a full stop is capitalized and all the numbers are written in brackets.
input_text = "this is a sentence. this is another sentence with 1234."

output_file = "formatted_output.txt"

try:
    formatted_text = ""
    capitalize_next = False

    for char in input_text:
        if char == '.':
            capitalize_next = True
            formatted_text += char
        elif capitalize_next and char.isalpha():
            formatted_text += char.upper()
            capitalize_next = False
        elif char.isdigit():
            formatted_text += f"({char})"
        else:
            formatted_text += char

    with open(output_file, "w") as file:
        file.write(formatted_text)

    print(f"Formatted data written to {output_file}.")
except IOError as e:
    print(f"Error writing to file: {e}")

# Question 8: Write a program that reads and copies the contents to another file, replacing all full stops with commas.
input_file = "input.txt"
output_file = "output_with_commas.txt"

try:
    with open(input_file, "r") as infile, open(output_file, "w") as outfile:
        for line in infile:
            outfile.write(line.replace('.', ','))

    print(f"File copied to {output_file} with full stops replaced by commas.")
except FileNotFoundError:
    print(f"Error: {input_file} not found.")
except IOError as e:
    print(f"Error reading/writing file: {e}")
