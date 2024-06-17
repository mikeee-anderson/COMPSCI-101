def main():
    filename = "names.txt"
    names = load_names(filename)
    display_menu()
    print("Welcome!")
    user_selection = get_user_selection()
    while user_selection != 0:
        if user_selection == 1:
            display_names(names)
            print()
        elif user_selection == 2:
            name_index = get_name_index(names)
            remove_name(names, name_index)
            print()
        user_selection = get_user_selection()
    save_names(filename, names)

def display_menu():
    print("----------------")
    print("1. Display names")
    print("2. Remove a name")
    print("0. Save & Exit")
    print("----------------")

display_menu()

def load_names(filename):
    input_file = open(filename, "r")
    # strip() gets rid of excess blank element in the list
    contents = input_file.read().strip()
    input_file.close()
    names = contents.split("\n")\
    return names

def display_names(name_list):
    for index in range(len(name_list)):
        print(f"{index + 1} : {name_list[index]}")

def remove_name(names_list, index):
    print("'{}' is removed.".format(names_list[index]))
    names_list.pop(index)

def save_names(filename, names_list):
    output_stream = open(filename, "w")
    for name in names_list:
        output_stream.write(name + "\n")
    output_stream.close()

def get_name_index(names_list):
    name_index = int(input("Enter an index: "))
    while name_index < 0 or name_index >= len(names_list):

def get_user_selection():
    user_selection = input("Enter a selection: ")
    while not (user_selection == "1" or user_selection == "2" or user_selection == "0"):
        user_selection = input("enter a selection: ")
    print()
    return int(user_selection)








main()