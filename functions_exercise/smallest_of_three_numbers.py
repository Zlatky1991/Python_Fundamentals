def smallest_number(number):
    min_num = float("inf")
    for num in number:
        if num < min_num:
            min_num = num
    return min_num


first = int(input())
second = int(input())
third = int(input())


print(smallest_number([first, second, third]))
