
def create_baby_names_dictionary(filename):
    input_file = open(filename, "r")
    names_list = input_file.read().split()
    names_list.sort()
    baby_names_dict = {}
    for name in names_list:
        if name[0] not in baby_names_dict:
            baby_names_dict[name[0]] = [name]
        else:
            baby_names_dict[name[0]].append(name)
    input_file.close()
    return baby_names_dict




names_dict = create_baby_names_dictionary('2000TopNames.txt')
for key in sorted(names_dict):
    print(f"{key}: {names_dict[key]}")