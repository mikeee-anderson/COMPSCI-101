colours = ["Red", "Yellow", "Green", "Purple", "Orange", "Cyan", "Magenta"]
print("Current list of colours:", colours)
new_colour = input("Enter a new colour: ")
insert_point = input("Enter the name of the colour you want to insert the new colour before: ")

if new_colour in colours:
    print("The new colour is already in the list or the preceding colour is not in the list.")
elif insert_point == "End":
    colours.append(new_colour)
    print(f"Updated list of colours: {colours}")
elif insert_point not in colours:
    print("The new colour is already in the list or the preceding colour is not in the list.")
else:
    index = colours.index(insert_point)
    colours.insert(index, new_colour)
    print(f"Updated list of colours: {colours}")

