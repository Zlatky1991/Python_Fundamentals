number_of_lines = int(input())

calculator = 0
for i in range(number_of_lines):
    liters_of_water = int(input())
    calculator += liters_of_water
    if calculator > 255:
        calculator -= liters_of_water
        print("Insufficient capacity!")
        continue
print(calculator)
