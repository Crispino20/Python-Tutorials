# Strings + len() + Slicing

# Exercise 1: Basic length
# - Store your name in a variable.
# - Print: "My name has X letters" (using len()).

my_name = "Crisp"
print("Exercise 1:")
print("My name has", str(len(my_name)) + " letters")


# Exercise 2: Indexing practice
# - Store "Python" in a variable.
# - Print the first letter, the last letter, and the middle letter(s).

character_index = 'Python'
print("Exercise 2:")
print("The first letter is", character_index[0])

# Exercise 3: Slicing practice
# - Store "Programming" in a variable.
# - Print:
# "Pro"
# "gram"
# "ing"

my_course = 'Programming'

print("Exercise 3:")
print(my_course[0:3])  # "Pro"
print(my_course[3:7])  # "gram"
print(my_course[8:11])  # "ing"


# Exercise 4: Step slicing
# Store "abcdefghij" in a variable.
# Print:
# - Every second letter
# - The string in reverse
alphabet = 'abcdefghij'

print("Exercise 4:")
print('Printing every second letter:', alphabet[::2])  # acegi
print('Printing the string in reverse:', alphabet[::-1])  # jihgfedcba

# Exercise 5: More step slicing
# word = "ABCDEFGHIJ"
# Print it in reverse.
# Print every 2nd character ("ACEGIJ").
# Print "FED" (using slicing, not hardcoding).

word = "ABCDEFGHIJ"
print('Exercise 5:')
# Reverse
print(word[::-1])
# Every second character
print(word[0::2])
# FED
print(word[3:6][::-1])


# Exercise 6 - Advanced step slicing
# use slicing to only reverse one word at a time? For example:
# "nohtyP Basics"
# "Python scisaB"

sentence = "Python Basics"
print('Exercise 6:')
print(f'{sentence[:6][::-1]} {sentence[7:]}')  # "nohtyP Basics"
print(f'{sentence[:6]} {sentence[7:][::-1]}')  # "Python scisaB"


# Exercise 7: Formatted String
# Using Formatted string, create variables for storing your name and age and print the output
name = 'Crispin'
age = 34
my_details = f'Hi, my name is {name} and I am {age} years old! I\'ll soon be turning {age + 1}!'
print('Exercise 7:')
print(my_details)
