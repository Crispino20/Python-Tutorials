# Strings + len() + Slicing

# Exercise 1: Basic length
# - Store your name in a variable.
# - Print: "My name has X letters" (using len()).

my_name = "Crisp"
print("# Exercise 1: Basic length")
print("My name has", str(len(my_name)) + " letters" + "\n")


# Exercise 2: Indexing practice
# - Store "Python" in a variable.
# - Print the first letter, the last letter, and the middle letter(s).

character_index = 'Python'
print("Exercise 2: Indexing practice")
print("The first letter is", character_index[0] + "\n")

# Exercise 3: Slicing practice
# - Store "Programming" in a variable.
# - Print:
# "Pro"
# "gram"
# "ing"

my_course = 'Programming'

print("Exercise 3: Slicing practice")
print(my_course[0:3])  # "Pro"
print(my_course[3:7])  # "gram"
print(my_course[8:11] + "\n")  # "ing"


# Exercise 4: Step slicing
# Store "abcdefghij" in a variable.
# Print:
# - Every second letter
# - The string in reverse
alphabet = 'abcdefghij'

print("Exercise 4: Step slicing")
print('Printing every second letter:', alphabet[::2])  # acegi
print('Printing the string in reverse:', alphabet[::-1] + "\n")  # jihgfedcba

# Exercise 5: More step slicing
# word = "ABCDEFGHIJ"
# Print it in reverse.
# Print every 2nd character ("ACEGIJ").
# Print "FED" (using slicing, not hardcoding).

word = "ABCDEFGHIJ"
print('Exercise 5: More step slicing')
# Reverse
print(word[::-1])
# Every second character
print(word[0::2])
# FED
print(word[3:6][::-1] + "\n")


# Exercise 6 - Advanced step slicing
# use slicing to only reverse one word at a time? For example:
# "nohtyP Basics"
# "Python scisaB"

sentence = "Python Basics"
print('Exercise 6: Advanced step slicing')
print(f'{sentence[:6][::-1]} {sentence[7:]}')  # "nohtyP Basics"
print(f'{sentence[:6]} {sentence[7:][::-1]} \n')  # "Python scisaB"


# Exercise 7: Formatted String
# Using Formatted string, create variables for storing your name and age and print the output
name = 'Crispin'
age = 34
my_details = f'Hi, my name is {name} and I am {age} years old! I\'ll soon be turning {age + 1}!'
print('Exercise 7: Formatted String')
print(my_details + "\n")

# Exercise 8: String methods (.upper(), .lower())
# Take the string 'course = 'python rogramming'
# Print it in all uppercase
# Print it in all lowercase
# Print just the first word "Python" (with a capital P).

course = 'python programming'
print("Exercise 8: .upper(), .lower()")
print(f'Uppercase - {course.upper()}')
print(f'Lowercase - {course.lower()}')
print(
    f'First letter of first word in uppercase - {course[0].upper()}{course[1:6]}\n')

# Exercise 9: String methods (strip(), replace())
# Take the string: messy = "   ***Python is fun!!!***   "
# Remove the leading/trailing spaces.
# Replace * with nothing (delete them).
# Print the cleaned version.

messy = "   ***Python is fun!!!***   "
print('Exercise 9: String methods (trim(), replace())')
print(f'Removing leading/trialing spaces - {messy.strip()}')
print(f'Replacing a character - {messy.replace("*", "")}')
print(f'Cleanup (removing leading space) - {messy.strip().replace("*", "")}\n')


# Exercise 10: String methods (replace(), count())
# Take the string: new_sentence = "I like Python because Python is powerful"
# Replace "Python" with "coding".
# Count how many times the word "Python" appears in the original sentence.

new_sentence = "I like Python because Python is powerful"
print('Exercise 10: String methods (replace(), count())')
print(f'Replace - {new_sentence.replace("Python", "coding")}')
print(f'Number of times Python appears - {new_sentence.count("Python")}\n')


# Exercise 11 – User Input Formatter (mini challenge with strip())
# Ask the user to enter their name (with extra spaces around it).
# Remove the spaces and print it with the first letter capitalized.

print('Exercise 11 – User Input Formatter (mini challenge with strip())')
print("Please enter your name with prefixed and suffixed spaces: ")
user_input = input()
stripped_input = user_input.strip()
print(f' The raw input is: {user_input}')
print(
    f' There are a total of {user_input.count(" ")} spaces in the text, and the length of the string is {(len(user_input))}')
print(f' The stripped input is: {stripped_input}')
print(
    f' There are a total of {stripped_input.count(" ")} spaces in the text, and the length of the string is {(len(stripped_input))}')
