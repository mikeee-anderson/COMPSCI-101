names = ["John", "Jane", "Peter", "Paul", "Michael", "Mary", "Robert", "Roland"]
print("Current list of names:", names)
command = input("Enter A to add a name or D to delete a name: ")

if command == "A":
    new_name = input("Enter a new name: ")
    add_point = input("Enter the name you want to insert the new name before: ")
    while add_point not in names:
        print(f"{add_point} is not in the list of names!")
        add_point = input("Enter the name you want to insert the new name before: ")
    names.insert(names.index(add_point),new_name)
    print(f"Updated list of names: {names}")
elif command == "D":
    remove_name = input("Enter a name to delete: ")
    while remove_name not in names:
        print(f"{remove_name} is not in the list of names!")
        remove_name = input("Enter a name to delete: ")
    names.pop(names.index(remove_name))
    print(f"Updated list of names: {names}")