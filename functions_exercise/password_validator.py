def number_of_characters(password):
    return 6 <= len(password) <= 10


def only_letters_and_digits(password):
    return password.isalnum() # It reads the input and checks if its only letters and numbers


def minimum_digits(password):
    numbers = 0
    for num in password:
        if num.isdigit(): # It reads the input and count all the digits into it
            numbers += 1
    return numbers >= 2


password_input = input()
flag = True

if not number_of_characters(password_input):
    flag = False
    print(f"Password must be between 6 and 10 characters")

if not only_letters_and_digits(password_input):
    flag = False
    print(f"Password must consist only of letters and digits")

if not minimum_digits(password_input):
    flag = False
    print(f"Password must have at least 2 digits")

if flag:
    print(f"Password is valid")
