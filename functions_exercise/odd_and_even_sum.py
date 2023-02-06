def even_and_odd_sum(num):
    even = 0
    odd = 0
    for num in num:
        number = int(num)
        if number % 2 == 0:
            even += number
        else:
            odd += number
    return [even, odd]


number_as_str = input()
result = even_and_odd_sum(number_as_str)

print(f"Odd sum = {result[1]}, Even sum = {result[0]}")
