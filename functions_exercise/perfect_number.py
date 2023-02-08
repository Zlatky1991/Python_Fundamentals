def perfect_number(number):
    num_calculator = []
    for el in range(1, number + 1):
        if number % el == 0:
            num_calculator.append(el)
    return sum(num_calculator)


num = int(input())

if perfect_number(num) - num == num:
    print("We have a perfect number!")
else:
    print(f"It's not so perfect.")
