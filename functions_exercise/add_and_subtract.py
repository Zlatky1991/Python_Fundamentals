def add(a, b):
    num = a + b
    return num


def subtract(a, b):
    subtract_num = a - b
    return subtract_num


first = int(input())
second = int(input())
third = int(input())

add_num = add(first, second)
final_result = subtract(add_num, third)


print(final_result)