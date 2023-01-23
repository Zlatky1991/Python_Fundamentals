import sys
output = ""
number_of_balls = int(input())
formula = 0
best_snowball = -sys.maxsize
for _ in range(number_of_balls):
    weight = int(input())
    time = int(input())
    quality = int(input())

    formula = (weight // time) ** quality
    if formula > best_snowball:
        best_snowball = formula
        output = f"{weight} : {time} = {best_snowball} ({quality})"

print(output)
