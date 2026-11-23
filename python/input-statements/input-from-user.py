# the input() function pauses the program and waits for the user to type something. whatever the user types is always returned as a string.

num1 = int(input("enter first number: "))   # by default input() always returns a string.
num2 = int(input("enter second number: "))  # we explicitly convert it into an integer.

# num1 = 100
# num2 = 200

total = num1 + num2
print(f"total: {num1 + num2}")
