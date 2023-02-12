word = [text for text in input() if text.lower() not in ['a', 'o', 'u', 'e', 'i']]

print("".join(word))