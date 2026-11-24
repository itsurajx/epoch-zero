"""
game: space cargo ship
description: a spaceship captain takes goods across planets to earn money.
"""

# take strings as input from user
captain_name = input("captain, enter your name: ")
spaceship_name = input("enter spaceship name: ")
name_of_a_planet = input("enter name of the planet: ")

# take numbers as input from user
cargo_boxes = int(input("enter number of cargo boxes: "))
crew_members = int(input("enter number of crew members: "))
price_per_box = float(input("enter price per cargo box: "))
fuel_cost_per_member = float(input("enter fuel cost per member: "))

# calculate cargo, fuel cost and profit
cargo_money = cargo_boxes * price_per_box
fuel_money = fuel_cost_per_member * crew_members
profit = cargo_money - fuel_money

# print outputs
print(
    f"i'm captain {captain_name} of the ship called {spaceship_name}. we are boarding from {name_of_a_planet} with the following cargo items.",
    end=" ",
)
print("gold", "water", "fuel", sep=" // ", end=".")
print(
    f" we are moving from planet {name_of_a_planet} to planet x. the total profit for this departure will be: {profit}. sending this information to the control room.",
    end="",
)
print("sending message", end="...")
print("success!")
