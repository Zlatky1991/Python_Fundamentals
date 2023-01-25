divisor = int(input())
max_number = int(input())

for i in range(max_number, 0, -1):
     if i % divisor == 0:
         print(i)
         break
