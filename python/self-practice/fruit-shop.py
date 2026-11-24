"""
game: fruit shop
description: you run a fresh fruit shop and need to make a bill for your customer.
"""

# take strings as input
customer_name = input("enter customer name: ")
favourite_fruit = input("enter customer's favourite fruit: ")
customer_city = input("enter customer city: ")

# take numbers as input
net_fruits = int(input("how many fruits do you want to buy: "))
net_shopping_bags = int(input("how many shopping bags do you need: "))
price_per_fruit = float(input("enter price of 1 fruit: "))
price_per_bag = float(input("enter price of 1 bag: "))

# calculate fruit bill & bag bill
fruit_bill = net_fruits * price_per_fruit
bag_bill = net_shopping_bags * price_per_bag
total_bill = fruit_bill + bag_bill

# print
print(
    f"hello, {customer_name}. nice to have you here, you are from {customer_city} & your favourite fruit is {favourite_fruit} right!",
    end="",
)
print(" here is our today's menu, i hope you like it: ", end="")
print("apple", "banana", "mango", sep=" - ", end="")
print(" okay you purchased these items, calculating the bill", end="...")
print(f" done!, total bill is: {total_bill}")
