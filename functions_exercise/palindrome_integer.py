def palindrome_integer(numbers):
    palindrome = []
    for numbers in numbers:
        if numbers[::-1] == numbers:
            numbers = "True"
            palindrome.append(numbers)
        else:
            numbers = "False"
            palindrome.append(numbers)

    return palindrome


num = input().split(", ")

result = palindrome_integer(num)

print(*result, sep="\n")
