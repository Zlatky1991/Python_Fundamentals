lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

helmet = 0
sword = 0
shield = 0
armor = 0

for _ in range(1, lost_fights + 1):

    if _ % 12 == 0:
        armor += 1
    if _ % 6 == 0:
        shield += 1
    if _ % 3 == 0:
        sword += 1
    if _ % 2 == 0:
        helmet += 1

total = helmet_price * helmet + sword_price * sword + armor_price * armor + shield_price * shield

print(f"Gladiator expenses: {total:.2f} aureus")
