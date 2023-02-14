random_numbers = input().split(", ")
even_num = [int(x) for x in random_numbers if int(x) % 2 == 0]
odd_num = [int(x) for x in random_numbers if int(x) % 2 != 0]
positive_num = [int(x) for x in random_numbers if int(x) >= 0]
negative_num = [int(x) for x in random_numbers if int(x) < 0]

print(f"Positive: {', '.join([str(x) for x  in positive_num])}")
print(f"Negative: {', '.join([str(x) for x in negative_num])}")
print(f"Even: {', '.join([str(x) for x in even_num])}")
print(f"Odd: {', '.join([str(x) for x in odd_num])}")