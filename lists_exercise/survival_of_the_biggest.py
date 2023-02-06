numbers_input = input().split()
num = int(input())
collected_numbers = []

for i in range(len(numbers_input)):
    collected_numbers.append(int(numbers_input[i]))
for el in range(1, num + 1):
    collected_numbers.remove(min(collected_numbers))

print(*collected_numbers, sep=", ")