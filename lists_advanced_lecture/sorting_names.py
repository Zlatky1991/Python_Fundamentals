names = input().split(", ")
sorting_list = sorted(names, key=lambda x: (-len(x), x))

print(sorting_list)