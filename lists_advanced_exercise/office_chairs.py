number = int(input())
chairs_counter = 0
flag = True
for num in range(1, number + 1):
    chairs_and_visitors = input().split(" ")
    if len(chairs_and_visitors[0]) < int(chairs_and_visitors[1]):
        flag = False
        print(f"{abs(len(chairs_and_visitors[0]) - int(chairs_and_visitors[1]))} more chairs needed in room {num}")

    else:
        chairs_counter += abs(len(chairs_and_visitors[0]) - int(chairs_and_visitors[1]))

if flag:
    print(f"Game On, {chairs_counter} free chairs left")




