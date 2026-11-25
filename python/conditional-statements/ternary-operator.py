# shorthand if-else: (ternary operator) -> python lets you write a simple if-else in a single line. this is called the ternary operator. it is useful when you want to assign a value based on a condition.

age = int(input("enter your age: "))
status = None

status = "adult" if age >= 18 else "minor"
print(status)
