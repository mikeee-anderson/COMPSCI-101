registered_upis = ["cron777", "emac263", "gclo450",
                "jcoc100", "jduj117", "lmes754", "mjac999"]
registered_passwords = ["SuiiiAlNassr23", "PcqcNP2022", "WhatElse06",
                "HatOn4414", "BlanQueTTe2006", "GoatWC2022", "thriLLer82"]
print("Current list of UPIs:", registered_upis)
print("Current list of passwords:", registered_passwords)

update = input("Enter A to add a UPI/password pair or D to delete a pair: ")

if update == 'A':
    new = input("Enter a new UPI: ")
    while new in registered_upis:
        print(f"{new} is already used!")
        new = input("Enter a new UPI: ")
    new_password = input("Enter a new password: ")
    registered_upis.append(new)
    registered_passwords.append(new_password)
    print(f"Updated list of UPIs: {registered_upis}")
    print(f"Updated list of passwords: {registered_passwords}")

elif update == 'D':
    delete = input("Enter the UPI to be deleted: ")
    while delete not in registered_upis:
        print(f"{delete} does not exist!")
        delete = input("Enter the UPI to be deleted: ")

    password = input("Enter the current password: ")
    while password != registered_passwords[registered_upis.index(delete)]:
        print("The password does not match!")
        password = input("Enter the current password: ")
    position = registered_upis.index(delete)
    registered_upis.pop(position)
    registered_passwords.pop(position)
    print(f"Updated list of UPIs: {registered_upis}")
    print(f"Updated list of passwords: {registered_passwords}")






