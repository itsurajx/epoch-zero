"""
game: the hero & magic shop
description: a hero goes on a quest and buys potions from a magic shop.
"""

# ask details in string
hero_name = input("enter your name: ")
adjective = input("enter adjective: ")
animal_name = input("enter monster/animal name: ")

# ask details in numbers
health_potions = int(input("enter required quantity of health potions required: "))
price_per_item = float(input("enter price of 1 potion: "))

# calculate total cost
total_cost = health_potions * price_per_item

# print using an f-string
print(f"there is a hero named {hero_name} in the city of lakes", end="...")
print(f" he has a backpack inside which he has some items", end="...")
print("sword", "shield", "potions", sep=" | ", end="...")
print(
    f" his objective was to be {adjective} but one day he got an animal whose name was {animal_name} & he purchased some potions for it which cost him {total_cost}"
)
