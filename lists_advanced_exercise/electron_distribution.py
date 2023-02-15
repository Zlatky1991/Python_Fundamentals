num_of_electrons = int(input())
shells_list = []

while num_of_electrons > 0:
    n = len(shells_list) + 1
    shel_value = min(2 *(n ** 2), num_of_electrons)
    shells_list.append(shel_value)
    num_of_electrons -= shel_value

print(shells_list)