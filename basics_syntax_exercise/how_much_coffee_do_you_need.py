result = 0

while True:
    command = input()

    if command == "END":
        break
    elif command == "cat" or command == "dog" or command == "coding" or command == "movie":
        result += 1
    elif command == "CAT" or command == "DOG" or command == "CODING" or command == "MOVIE":
        result += 2
    else:
        continue

if result > 5:
    print("You need extra sleep")
else:
    print(result)