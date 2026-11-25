# q12: take three numbers as input. print the largest of the three without using any built-in function.
a = int(input("enter first number: "))
b = int(input("enter second number: "))
c = int(input("enter third number: "))

if a == b and b == c:
    print(f"{a}, {b}, {c} all are equal, no greatest found.")
elif a >= b and a >= c:
    print(f"{a} is greatest.")
elif b >= a and b >= c:
    print(f"{b} is greatest.")
else:
    print(f"{c} is greatest.")
