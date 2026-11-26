# game: cinema ticker and snack counter
# story: you run a ticket counter at a cinema. you need to check the customer's age for movie rating, calculate ticket prices. check for discounts, and print their final receipt.

# take inputs
name = input("enter you're name: ")
age = int(input("enter you're age: "))
tickets = int(input("enter no of total tickets: "))
price = int(input("enter price of a ticket: "))
has_student_pass = input("do you have student pass (yes/no): ")

# condition and checks
if age < 12:
    print("too young for this movie!")
else:
    print("they can watch!")
    # math & discounts
    ticket_total = tickets * price
    discount = None
    if has_student_pass == "yes" or age >= 60:
        discount = 0.1
        ticket_total = ticket_total - (ticket_total * 0.1)
    elif tickets >= 5:
        discount = 0.05
        ticket_total = ticket_total - (ticket_total * 0.05)
    else:
        discount = 0.00
        ticket_total = ticket_total - (ticket_total * 0.00)

    # print receipt:
    print("print ticket", end="...")
    print("done.")
    print("row-a", "seat-01", "screen-02", sep="|")
    print("row-a", "seat-02", "screen-02", sep="|")
    print("row-a", "seat-03", "screen-02", sep="|")

    print(f"""
                reciept
        total_price : {tickets * price}
        discount    : {discount*100}%
        amount      : {ticket_total}
    """)
