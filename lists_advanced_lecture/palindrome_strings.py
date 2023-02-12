words_received = input().split(" ")
palindrome_word = input()
palindrome_list = [word for word in words_received if word[::-1] == word]
counter = 0

for searching_for_palindrome in palindrome_list:
    if searching_for_palindrome == palindrome_word:
        counter += 1

print(palindrome_list)
print(f"Found palindrome {counter} times")
