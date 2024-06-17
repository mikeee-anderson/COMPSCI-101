num_list = [11, 25, 64, 22, 9]
def move_largest_to_end(number_list):
    high = max(number_list)
    index = number_list.index(max(number_list))
    number_list.pop(index)
    number_list.append(high)

print(f"Before: {num_list}")
move_largest_to_end(num_list)
print(f"After: {num_list}")