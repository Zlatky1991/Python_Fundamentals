number = int(input())
comma = ","
line = "_"
dot = "."
for i in range(number):
    string = input()

    if comma in string or line in string or dot in string:
        print(f"{string} is not pure!")
    else:
        print(f"{string} is pure.")