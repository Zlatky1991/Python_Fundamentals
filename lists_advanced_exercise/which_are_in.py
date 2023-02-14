first_sequence = input().split  (", ")
second_sequence = input().split(", ")
substrings = []

for word in first_sequence:
    for second_word in second_sequence:
        if word in second_word:
            substrings.append(word)
            break

print(substrings)