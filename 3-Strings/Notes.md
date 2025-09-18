# Strings 

- If you want to reference a quote within a string, you can opt for single quote on the outside text and double for the quoted text or use double quote for the outside text and single for the quoted text e.g `'John said "Bring the cat tomorrow"'` or `"John said 'Bring the cat tomorrow'"`. Alternatively, if you want to use double quotes for a quote you can use an *escape character* e.g `"John said "Python \"Programming\""`
- If you want to add a back slash in a string, you can also use an escaped character e.g `"Document\\Python"`
- To add a new line in a string, use an escaped character e.g `"Python \nProgramming`
- Use triple quotes for very long multi line strings
- Functions are built in functions that perform a task
  - You can use the `len` function to return the length of characters in a string e.g `print(len(course))`

## Python Slicing
- Use Python slicing to get a subset of a string e.g Given `Course = Physics`
  - Obtaining first character in the string: `print(course[0])` - This will output "P"
  - Slicing syntax 
    - [0:3] - The first index is the starting index and the second after the colon is the end index 
    - [::2] - The third index in this format represents the step interval. In this example it returns the first character in the index and every second character after that. 
  - Obtaining first 3 characters in the string: `print(course[0:3])` - This will output "Phy"

## Formatted strings
- Formatted strings can be used in place of regular strings `full = f'{first_name} {last_name}'`

## String methods 
- string object methods can be accessed using the `"."` notation
- **.upper()** converts string text to uppercase 
- **.lower()** converts string text to lowercase 
- **.title()** capitalises the starting letter of each word e.g `Python Programming`
- **.strip()** is used to trim any white space at the beginning and end of a string
- **.lstrip()** removes the white space at the beginning of a string 
- **.rstrip()** removes the white space at the end of a string 
- **.find()** To get the **index** of a character or a sequence of characters in the string e.g `print(course.find("Pyt"))`
- **.replace()** returns a new string with specified character(s) replaced by another; it does not modify the original string in place (Bear in mind that this is case sensitive)
- **in** finds the existence of a character or a string of characters in your expression and returns a boolean value e.g `"pro" in course`
- **not** Used to check if the string does not contain a character or string of characters in an  expression and returns a boolean value e.g `"pro" not in course`




