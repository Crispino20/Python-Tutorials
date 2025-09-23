# Numbers 
There are 3 types of numbers in Python
1. Integer
2. Float e.g 1.1
3. Complex numbers e.g x = a + bi (where i is the imaginary number)

## Common operators 
- **Addition**: e.g                    `print(10 + 3)`
- **Subtraction** e.g                  `print(10 - 3)`
- **Multiplication** e.g               `print(10 * 3)`
- **Division** e.g                     `print(10 / 3)`. Returns 3.33333xx
- **Division (whole number only)** e.g `print(10 // 3)`. Returns 3
- **Modulus (Remainder)** e.g                    `print(10 % 3)`. Returns 1
- **Exponent (power)** e.g `print(10 ** 3)`. Returns 1000

## Augmented assignment operator 
The augmented assignment operator is a shorthand and cleaner way of assigning variables.
Consider the below expression:
```
x = 10
x = x + 3 
print(x) # 13
```

With augmented  assignement operator, the above can be rewritten as follows:
```
x = 10
x += 3 
print(x) # 13
```

## Working with numbers 
There are several mathematical methods available in Python. Most of which need to be imported using the math module. At the top of the python file, import the module by entering `import math`. The functions can then be accessed by typing `math.xx`. 
A list of math modules can be found [here](https://docs.python.org/3/library/math.html)
### Methods 
- **Round**: used for rounding numbers e.g `print(round(2.9))`
- **Abs**: used for printing the absolute value of an expression. The output is always positive e.g `print(abs(-2.9))`. This outputs 2.9
- **Ceil**: This function rounds a number up to the nearest whole number e.g `print(math.ceil(2.2))`. This outputs 3.                              