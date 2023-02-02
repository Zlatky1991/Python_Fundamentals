numbers = input().split(", ")
num = int(input())
beggars = [0] * num

for el in range(len(numbers)):
    calculation = el % num
    count = int(numbers[el])
    beggars[calculation] += count
print(beggars)
