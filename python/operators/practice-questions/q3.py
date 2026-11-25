# q3: take the user's age as input. check and print whether they are eligible to vote (age >= 18) and whether they are a senior citizen (age >= 60). print both results.

age = int(input("enter your age: "))

print(f"eligible to vote: {age >= 18}")
print(f"senior citizen: {age >= 60}")
