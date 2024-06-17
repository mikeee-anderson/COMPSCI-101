line1 = input("Enter the first line of data: ")
line2 = input("Enter the second line of data: ")

new_list = []
list_line1 = line1.split()
list_line2 = line2.split()

for i in range(len(list_line1)):
    if (list_line1[i].isdigit() or list_line1[i].startswith("-")) and (list_line2[i].isdigit() or list_line2[i].startswith("-")):
        digit1 = int(list_line1[i])
        digit2 = int(list_line2[i])
        new_list += [digit1 + digit2]
    else:
        concated =list_line1[i] + "" + list_line2[i]
        new_list += [concated]

print(f"The merged data is: {new_list}")

