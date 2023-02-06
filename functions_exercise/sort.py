def sorting_numbers(numbers):
    sorting_list = []
    for numbers in numbers:
        sorting_list.append(int(numbers))
    return sorted(sorting_list)


numbers_to_sort = input().split(" ")

result = (sorting_numbers(numbers_to_sort))

print(result)

