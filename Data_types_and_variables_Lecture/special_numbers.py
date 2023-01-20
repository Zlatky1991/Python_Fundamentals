num = int(input())

for i in range(1, num + 1):
    is_special = False
    sum_numbers = 0
    num_str = str(i)

    for char in num_str:
        sum_numbers += int(char)

    if sum_numbers == 5 or sum_numbers == 7 or sum_numbers == 11:
        is_special = True

    print(f"{i} -> {is_special}")