def parameters(text, num_one, num_two):
    if text == "multiply":
        return num_one * num_two
    elif text == "divide":
        return num_one // num_two
    elif text == "add":
        return num_one + num_two
    elif text == "subtract":
        return num_one - num_two


order = input()
first = int(input())
second = int(input())

print(parameters(order, first, second))

