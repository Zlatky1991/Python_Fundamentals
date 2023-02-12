notes = [0] * 10


while True:
    command = input()
    if command == "End":
        break
    priority, task = command.split("-")
    priority = int(priority)
    index = priority - 1
    notes[index] = task

print([el for el in notes if el != 0])

