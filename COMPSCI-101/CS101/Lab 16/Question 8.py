email_dict = {"Damir":"damir@mail.com", "Ann":"ann@mail.com"}
phone_num_dict = {'Damir':"021-1234567", "Ann":"022-1234567"}


def merge_dictionaries(email_dict, phone_num_dict):
    # Create a new dictionary to store the merged results
    merged_dict = {}

    # Loop through the keys of one of the dictionaries (both have the same keys)
    for key in email_dict:
        # Create a tuple with the email and phone number
        merged_dict[key] = (email_dict[key], phone_num_dict[key])

    return merged_dict


contacts_dict = merge_dictionaries(email_dict, phone_num_dict)
for key in sorted(contacts_dict):
    print(key, contacts_dict[key])
print(type(contacts_dict))