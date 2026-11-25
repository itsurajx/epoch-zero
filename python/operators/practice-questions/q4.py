# q4: a student scored marks in 3 subjects. take all three as input, calculate the total and average, and print both using an f-string.
physics = int(input("enter marks of physics: "))
chemistry = int(input("enter marks of chemistry: "))
mathematics = int(input("enter marks of mathematics: "))

print(
    f"the average of all your three subjects is: {(physics + chemistry + mathematics) // 3}"
)
