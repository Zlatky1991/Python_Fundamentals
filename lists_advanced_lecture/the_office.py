employees = input().split(" ")
factor = int(input())
mapping_list = []
total_count = 0
happy_count = 0
for num in employees:
    total_count += 1
    mapping = int(num) * factor
    mapping_list.append(mapping)

average = sum(mapping_list) / total_count

for idx in mapping_list:
    if idx >= average:
        happy_count += 1

if total_count / 2 <= happy_count:
    print(f"Score: {happy_count}/{total_count}. Employees are happy!")
else:
    print(f"Score: {happy_count}/{total_count}. Employees are not happy!")
