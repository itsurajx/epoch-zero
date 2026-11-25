"""
q14: a shop gives discounts based on purchase amount:
above 5k -> 20% discount.
above 2k -> 10% discount.
above 1k -> 5% discount.
1k or below -> no discount.
"""

amount = int(input("enter amount: "))

if amount > 5000:
    print("congrats, you got a discount of 20%.")
    print(f"you just have to pay: {amount - (amount * 20 // 100)}")
elif amount > 2000:
    print("congrats, you got a discount of 10%.")
    print(f"you just have to pay: {amount - (amount * 10 // 100)}")
elif amount > 1000:
    print("congrats, you got a discount of 5%.")
    print(f"you just have to pay: {amount - (amount * 5 // 100)}")
elif amount >= 0:
    print("sorry, you got no discount.")
    print(f"you just have to pay: {amount}")
else:
    print("enter a valid amount.")
