a_dict = {"a":0, "b":0, "c":1, "d":1, "e":5}
print("Before:", end=" ")
keys = list(a_dict.keys())
for key in keys:
    print(f"{key}:{a_dict[key]}", end=" ")
print()

def update_dictionary(a_dict, target_value):
    keys_list = list(a_dict)
    for key in keys_list:
        if a_dict.get(key) == target_value:
            del a_dict[key]
    return a_dict




update_dictionary(a_dict, 0)
print("After:", end=" ")
keys = list(a_dict.keys())
for key in keys:
    print(f"{key}:{a_dict[key]}", end=" ")
print()