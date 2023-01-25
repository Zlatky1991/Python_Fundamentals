quantity = int(input())
days_left = int(input())

ornament_set = 2
tree_skirt = 5
tree_garlands = 3
tree_lights = 15

money = 0
points = 0

for i in range(1, days_left + 1):
    if i % 11 == 0:
        quantity += 2

    if i % 10 == 0:
        points -= 20
        money += tree_skirt + tree_garlands + tree_lights

        if i == days_left:
            points -= 30

    if i % 5 == 0:
        money += quantity * tree_lights
        points += 17

    if i % 15 == 0:
        points += 30

    if i % 3 == 0:
        money += (quantity * tree_skirt) + (quantity * tree_garlands)
        points += 3 + 10

    if i % 2 == 0:
        money += quantity * ornament_set
        points += 5
print(f"Total cost: {money}")
print(f"Total spirit: {points}")