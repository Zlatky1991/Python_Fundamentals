from math import ceil

sequence_num = input().split(", ")
original_list = [int(x) for x in sequence_num]

min_boundary = 1
max_boundary = 10
groups_count = ceil(max(original_list) / 10)

for i in range(1, groups_count + 1):
    result = [int(x) for x in original_list if min_boundary <= int(x) <= max_boundary]
    print(f"Group of {i * 10}'s: {result}")
    min_boundary += 10
    max_boundary += 10



