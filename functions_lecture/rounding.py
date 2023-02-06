numbers = input().split()
my_list = []
for i in numbers:
    my_list.append(i)


round_the_whole_list = []
for num in my_list:
    round_the_whole_list.append(float(num))

new_list = [round(num_two) for num_two in round_the_whole_list]

print(new_list)