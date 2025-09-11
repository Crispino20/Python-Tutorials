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
