# game: smart electricity bill calculator
# story: calculate the montly electricity bill for a house based on units used, with bonus solar discounts and penalty checks.

# take inputs
name = input("enter you're name: ")
units = float(input("how many units of electricity were used this month: "))
has_solar_panel = input("do you have solor panel installed (yes/no): ")
has_payment_due = input("do you have any payment due (yes/no): ")

# calculate rate
base_bill = None
price = 10.0
if units <= 100:
    price = 5.0
    base_bill = units * price
elif units <= 300:
    price = 7.5
    base_bill = units * price
else:
    base_bill = units * price

# discounts and penalties
discount = 0
if has_solar_panel == "yes" and units < 200:
    discount = 50.0
    base_bill = base_bill - discount
penalties = 0
if has_payment_due == "yes":
    penalties = 30.0
    base_bill = base_bill + penalties

# print bill
print("equipment: ", "fan", "lights", 'ac', "tv", sep="|")
print("generating bill", end="...")
print("compelete!")
print(f"""
            bill
    units       :   {units} unit
    price       :   Rs. {price} per unit
    discount    :   Rs. {discount}
    penalties   :   Rs. {penalties}
    amount      :   Rs. {base_bill}
""")

