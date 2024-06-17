item = input("Please enter an item for your shopping list or end to print the list: ")
shopping_list = []
while item != "end":
    shopping_list.append(item)
    item = input("Please enter an item for your shopping list or end to print the list: ")


shopping_list.sort()
counter = 0
amount = 1
print(" ")
print("Shopping List:")
print("==============")
while counter < len(shopping_list):
    print(f"{amount}) {shopping_list[counter]}")
    counter += 1
    amount += 1
