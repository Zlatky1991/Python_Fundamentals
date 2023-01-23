num = int(input())
calculator = 0
for i in range(1, num + 1):
    letter = input()
    calculator += ord(letter)

print(f"The sum equals: {calculator}")
