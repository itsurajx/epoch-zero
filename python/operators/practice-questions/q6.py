# q6: take two numbers as input. without using *, calculate and print their product using += in a way that adds the first number to itself the second number times.

a = int(input("enter first number: "))
b = int(input("enter second number: "))

result = 0
for i in range(b):
    result += a

print(f"the product is: {result}")
