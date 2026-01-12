# Logical operators are used to combine conditional statements
# or to reverse the result of a condition.

# Assigning integer values to variables
a = 50
b = 30

# Logical NOT operator:
# 'not True' reverses the boolean value.
# Since True becomes False, this will print False.
print(not True)

# Logical NOT with a condition:
# (a > b) checks whether 50 is greater than 30, which is True.
# 'not' reverses True to False, so this will print False.
print(not (a > b))

# Assigning boolean values to variables
val1 = True
val2 = True

# Logical AND operator:
# 'and' returns True only if BOTH values are True.
# Here both val1 and val2 are True, so the result is True.
print("answer :", val1 and val2)

# Logical OR operator:
# 'or' returns True if AT LEAST ONE value is True.
# Here both values are True, so the result is True.
print("answer :", val1 or val2)

# Logical OR with comparison expressions:
# (a == b) checks if 50 is equal to 30 → False
# (a > b) checks if 50 is greater than 30 → True
# False OR True results in True.
print("answer :", (a == b) or (a > b))
