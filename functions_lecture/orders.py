def parameter(text, number):
    if text == "coffee":
        return number * 1.50
    elif text == "coke":
        return number * 1.40
    elif text == "water":
        return number * 1.00
    elif text == "snacks":
        return number * 2.00


order = input()
quantity = int(input())
print(f"{parameter(order, quantity):.2f}")
