received_text = input().split(" ")
filtered_list = [x for x in received_text if len(x) % 2 == 0]
print("\n".join(filtered_list))
