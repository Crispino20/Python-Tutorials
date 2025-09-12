course = "Python Programming"
message = """
I am learning Python and it's fun!
Looking forward to mastering it.

"""
# Print out the variables
print(course)
print(message)

# Obtain the length of the string
print('The length of the Course string is: ' + str(len(course)))
print('The length of the Message string is: ' + str(len(message)))

# Python slicing - obtaining a subset of a string

# Get the letter of the first character in the course string
print(course[0])
# Get the letter of the last character in the course string
print(course[-1])
# Get the first 6 characters of the course string
# 0 represents the starting index and 6 represents the ending index (not inclusive)
print(course[0:6])
# Get all the characters from the starting index to the end of the string
print(course[0:])  # Python Programming
# Get all the characters from the starting index to the ending index (not inclusive)
print(course[:3])  # Pyt
# Get all the characters in the string
print(course[:])  # Python Programming
# Get every second character in the string
print(course[::2])  # Pto rgamn
print(course[1::3])  # yoPgmn


this_text = "Python \"Programming\""
print(this_text)

document_path = "Document\\Python"
print(document_path)

new_line = "Python \nProgramming"
print(new_line)
