# Day 2: Python Data Types Practice
# This program dwmonstrates int, float, str, bool and how to check type

# Integer
age = 20           # Assign integer 20 to variable 'age'
print(age)         # Print the value of age - output: 20
print(type(age))   # Print the data type of age - output: <class 'int'>
# NOTE: type() fuction is used to check the data type of a value or variable.
# Common mistake: beginners often forget the parentheses and write print(type) which does NOT show variable type.

price = 90.99      
print(price)
print(type(price))
# NOTE: forgetting that numbers with decimals are floats, not int.

name = "agrojit"
print("agrojit")
print(type(name))
# NOTE: printing the variable name vs printing the string directly.
# print(name) would print the variable's value, whereas print("agrojit") prints the literal string.

is_student = True
print(is_student)
print(type(is_student))
# NOTE: True and False are case-sensitive. Writing 'true' or 'false' will cause an error.
