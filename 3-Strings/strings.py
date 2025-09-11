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

length = 10
width = 30
perimeter = 2 * (length + width)
print("The perimeter of the rectangle is:", perimeter)

my_course = "Programming"
print(my_course[0:3])
print(my_course[3:7])
print(my_course[8:11])


# Step slicing
alphabet = "abcdefghi"
print('Every second letter: ', alphabet[::2])
print('String in reverse: ', alphabet[::-1])

# Len
text = "Hello World"
print(len(text[0:5]))  # 5
print(text[0:5])  # Hello
print(len(text[6:11]))  # 11
print(text[6:11])  # World
