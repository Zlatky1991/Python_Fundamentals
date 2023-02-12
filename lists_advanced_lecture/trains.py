wagons = int(input())
train_list = [0] * wagons
command = input()
while command != "End":
    action = command.split()[0]
    if action == "add":
        num_people = int(command.split()[1])
        train_list[-1] += num_people
    elif action == "insert":
        num_people = int(command.split()[2])
        idx = int(command.split()[1])
        train_list[idx] += num_people
    elif action == "leave":
        num_people = int(command.split()[2])
        idx = int(command.split()[1])
        train_list[idx] -= num_people

    command = input()

print(train_list)



