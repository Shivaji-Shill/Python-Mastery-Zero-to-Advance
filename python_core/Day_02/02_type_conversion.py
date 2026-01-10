# Day 2: Type Conversion Practice
# input() always returns string
# we convert string to int/float to do calculations

# User input
age = input("Enter your age: ")  # Input is always string
print("Your input type:", type(age))

# Convert string to integer
age = int(age)
print("After converting to int:", age)
print("Type now:", type(age))

# Convert integer to string
age_str = str(age)
print("Integer to string:", age_str)
print("Type now:", type(age_str))

# Convert integer to float
age_float = float(age)
print("Integer to float:", age_float)
print("Type now:", type(age_float))

