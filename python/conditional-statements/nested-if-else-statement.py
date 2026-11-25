# nested if-else statement: you can place an if statement inside another if statement. this is called nesting and is useful when a second condition only makes sense if the first one is already true.

age = 22
has_degree = True

if age >= 18:
    print("age requirement met.")
    if has_degree:
        print("you are eligible for this job.")
        # pass: in future want to write something.
    else:
        print("you need a degree for this job.")
else:
    print("you are too young to apply.")
