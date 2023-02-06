def find_even_number(num):
    list_even_num = []
    for num in num:
        digit = int(num)
        if digit % 2 == 0:
            list_even_num.append(digit)
    return list_even_num


number_as_string = input().split(" ")

print(find_even_number(number_as_string))
