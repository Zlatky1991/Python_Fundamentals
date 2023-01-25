orders = int(input())
total = 0
for i in range(orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_needed_per_day = int(input())
    if 0.01 <= price_per_capsule <= 100 and 1 <= days <= 31 and 1 <= capsules_needed_per_day <= 2000:
        coffee_price = price_per_capsule * days * capsules_needed_per_day
        total += coffee_price
        print(f"The price for the coffee is: ${coffee_price:.2f}")
    else:
        continue

print(f"Total: ${total:.2f}")
