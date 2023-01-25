result = " "
while True:
    string = input()

    if string == "End":
        break
    elif string == "SoftUni":
        continue
    for letters in string:
        result = letters*2
        print(result, end="")
    print()
