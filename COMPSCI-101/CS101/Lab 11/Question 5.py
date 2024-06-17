def get_user_selection():
    selection = int(input("Enter your selection: "))
    while selection < 0 or selection > 7:
        print("Invalid selection!")
        selection = int(input("Enter your selection: "))
    return selection

print(type(get_user_selection()))
print(get_user_selection())



