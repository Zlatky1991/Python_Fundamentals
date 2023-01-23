
group_size = int(input())
days = int(input())
coins = 0

for _ in range (1, days + 1):
    if _ % 10 == 0:
        group_size -= 2

    if _ % 15 == 0:
        group_size += 5
        coins -= 2 * group_size


    coins += 50 - 2 * group_size

    if _ % 3 == 0:
        coins -= 3 * group_size

    if _ % 5 == 0:
        coins += 20 * group_size


coins_total = coins // group_size

print(f"{group_size} companions received {coins_total} coins each.")
