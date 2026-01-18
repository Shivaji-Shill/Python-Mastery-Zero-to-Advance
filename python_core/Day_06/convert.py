# Use input() to take a string from the user and .split() to break it into parts based on spaces
# Use map(int, ...) to convert those string parts into actual integers (numbers)
# Finally, assign the two numbers to variables 'a' and 'b'
a, b = map(int, input("Enter two numbers: ").split())

# Display the value stored in variable 'a'
print("First number:", a)

# Display the value stored in variable 'b'
print("Second number:", b)