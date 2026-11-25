# q8: take two numbers as input. print the greater of the two. if they are equal, print both are equal.
num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))

if num1 > num2:
    print(f"{num1} is greater.")
elif num2 > num1:
    print(f"{num2} is greater.")
else:
    print(f"{num1} and {num2} both are equal.")
