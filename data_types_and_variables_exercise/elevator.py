from math import ceil
number_of_people = int(input())
capacity = int(input())

courses_needed = number_of_people / capacity
print(ceil(courses_needed))

