number = int(input())
positive = []
negative = []

for i in range(number):
    n = int(input())

    if n >= 0:
        positive.append(n)
    else:
        negative.append(n)

print(positive)
print(negative)
print(f"Count of positives: {len(positive)}")
print(f"Sum of negatives: {sum(negative)}")