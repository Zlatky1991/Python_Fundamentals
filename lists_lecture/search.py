num = int(input())
word = input()
string_containing_word = []
my_list = []
for i in range(num):
    current_word = input()
    my_list.append(current_word)
    if word in current_word:
        string_containing_word.append(current_word)
print(my_list)
print(string_containing_word)