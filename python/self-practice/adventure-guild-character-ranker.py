# game: adventure guild character ranker
# story: a warrior joins a guild. based on their level, good coins, and battes wonm determine their warrier badge and membership status.

# take inputs
warrior_name = input("enter warrior name: ")
character_level = int(input("enter character level: "))
battels_won = int(input("enter no of battels you won: "))
gold_coin = int(input("enter no of gold coins you carry: "))

# assign rank
rank = "apprentice"
if character_level >= 20 and battels_won >= 50:
    rank = "diamond knight"
elif character_level >= 10 or battels_won >= 20:
    rank = "silver warrior"
elif character_level >= 5:
    rank = "bronze rookie"
else:
    rank = "apprentice"

# calculation
loose_coins = gold_coin % 10
full_bags = gold_coin // 10

# print
print("equipment items: ","swords", "bows", "staffs",  "daggers", sep=" -> ")
print(f"message status", end="...")
print(f"""
        you're details
    rank name   :   {rank}
    full bags   :   {full_bags}
    leftover    :   {loose_coins}   
""")