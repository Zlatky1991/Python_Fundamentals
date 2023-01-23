num = int(input())

letter1 = ""
letter2 = ""
letter3 = ""
for i in range(0, num):
    letter1 = chr(97 + i)
    for j in range(0, num):
        letter2 = chr(97 + j)
        for k in range(0, num):
            letter3 = chr(97 + k)
            print(f"{letter1}{letter2}{letter3}")

