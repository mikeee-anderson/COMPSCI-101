line_of_data = input("Enter your data: ")
list_of_data = line_of_data.split()

new_list = []
for i in range(len(list_of_data)):
    if list_of_data[i].isdigit():
        list_of_data[i] = int(list_of_data[i])
        new_list += [list_of_data[i]]
    else:
        new_list += [list_of_data[i]]

print(f"List of data: {new_list}")