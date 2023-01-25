budget = float(input())
flour = float(input())

one_pack_eggs = flour * 0.75
one_liter_milk = (flour * 1.25) * 0.25

easter_bread = flour + one_liter_milk + one_pack_eggs
bread_counter = 0
colored_eggs = 0
while easter_bread <= budget:
    colored_eggs += 3
    budget -= easter_bread
    bread_counter += 1
    if bread_counter % 3 == 0:
        colored_eggs -= (bread_counter - 2)

print(f"You made {bread_counter} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
