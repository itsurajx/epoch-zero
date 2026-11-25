# q11: take a person's age and whether they have a valid id (yes/no) as input. they can enter a venue only if they are 18 or older and have a valid id. print the appropriate message.

age = int(input("enter your age: "))
valid_id = input("do you have a valid id (yes/no): ")

if age >= 18 and valid_id.lower() == "yes":
    print("you can enter the venue.")
else:
    print("you cannot enter the venue, please meet the requirement.")
