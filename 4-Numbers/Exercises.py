import math
# Exercise 1: Shopping Bill
# A customer buys:
# Apples for $2.75
# Bread for $1.20
# Milk for $3.40

# Write a program that:
# Stores each price in a variable.
# Calculates the total.
# Prints the total using both round(total, 2) and math.ceil(total).

print('Exercise 1: Shopping Bill')
apples = 2.75
bread = 1.20
milk = 3.40
total = apples + bread + milk

print(f'Your shopping list total is ${total}')
print(
    f'The rounded value of your total to two decimal places is ${round(total, 2)}')
print(f'The ceiling value of your total is ${math.ceil(total)} \n')


# Exercise 2: Temperature Difference
# You record the temperature on two days:
# Day 1 = 15°C
# Day 2 = -3°C

# Write a program that:
# Calculates the difference between the two temperatures.
# Uses abs() to show the difference as a positive number.

print('Exercise 2: Temperature Difference')
day_1 = 15
day_2 = -3
difference_in_temp = abs(day_1 - day_2)
print(
    f'The difference in temperature is: {difference_in_temp} degrees \n')

# Exercise 3: Height Conversion
# A person’s height is 175.5 cm.
# Convert this height to meters (divide by 100).
# Print the result rounded to 2 decimal places.
# Print the result using math.floor() and math.ceil() to show the lower and upper bounds.
print('Exercise 3: Height Conversion')
height_in_cm = 175.5
height_to_meters = height_in_cm/100
height_to_meters_rounded = round(height_to_meters/100, 2)
height_to_meters_floor = math.floor(height_to_meters)
height_to_meters_ceil = math.ceil(height_to_meters)

print(f'John is {height_to_meters_rounded} meters tall')
print(f'John\'s floor height is {height_to_meters_floor} meter(s)')
print(f'John\'s ceil height is {height_to_meters_ceil} meter(s) \n')

# Exercise 4: Mini Project: Trip Cost Calculator
# Imagine you’re planning a road trip.
# Store the following values in variables:
# Distance = 420.7 km
# Fuel consumption = 6.4 liters per 100 km
# Fuel price = 1.85 dollars per liter

# Calculate:
# The total liters of fuel needed.
# The total fuel cost.
# Round the cost to 2 decimal places.
# Use:
# abs() → Just to make sure distance is treated as positive.
# math.floor() and math.ceil() → to show cost rounded down and up

distance = 420.7
fuel_consumption = 6.4
fuel_price = 1.85

fuel_needed = round((distance/100) * fuel_consumption, 1)
fuel_cost = (round(fuel_price * fuel_needed, 2))
fuel_cost_floor = math.floor(fuel_cost)
fuel_cost_ceil = math.ceil(fuel_cost)

print('Exercise 4: Mini Project: Trip Cost Calculator')
print(f'Trip Distance: {distance} km')
print(f'Fuel Needed: {fuel_needed} litres')
print(f'Fuel cost (rounded): ${fuel_cost}')
print(f'Fuel cost (floor): ${fuel_cost_floor}')
print(f'Fuel cost (ceil): ${fuel_cost_ceil}')
