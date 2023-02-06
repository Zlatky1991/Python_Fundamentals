numbers = input().split(", ")
my_list = []
new_list = []
zero = []
for i in numbers:
    my_list.append(i)

for num in my_list:
    if num != '0':
        new_list.append(int(num))
    else:
        zero.append(int(num))

print(new_list+zero, sep=", ")
