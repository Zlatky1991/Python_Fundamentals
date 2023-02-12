numbers = input().split(", ")
total_list = []
indices_list = []

for el in numbers:
    total_list.append(int(el))
for idx in range(len(total_list)):
    if total_list[idx] % 2 == 0:
        indices_list.append(idx)

print(indices_list)