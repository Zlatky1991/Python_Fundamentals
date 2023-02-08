def loading_bar(percent):
    bar = "[" + "%" * (percent // 10) + "." * (10 - percent // 10) + "]"
    return bar


number = int(input())
result = loading_bar(number)

if number == 100:
    print("100% Complete!")
    print(result)
else:
    print(f"{number}% {result}")
    print("Still loading...")