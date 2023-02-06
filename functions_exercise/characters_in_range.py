def characters_in_between(a, b):
    my_list_of_char = []

    for el in range(ord(a) + 1, ord(b)):
        my_list_of_char.append(chr(el))

    return my_list_of_char


first_char = input()
second_char = input()

result = characters_in_between(first_char, second_char)

print(" ".join(result))
