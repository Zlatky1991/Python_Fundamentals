def min_max_sum(numbers):
    list_of_numbers = []
    for numbers in numbers:
        list_of_numbers.append(int(numbers))
    return list_of_numbers


num = input().split(" ")

min_number = min_max_sum(num)
max_number = min_max_sum(num)
sum_number = min_max_sum(num)

print(f"The minimum number is {min(min_number)}")
print(f"The maximum number is {max(max_number)}")
print(f"The sum number is: {sum(sum_number)}")
