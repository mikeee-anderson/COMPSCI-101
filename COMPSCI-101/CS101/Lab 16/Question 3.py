
def create_baby_names_dictionary(filename):
    input_stream = open(filename, "r")
    names_list = input_stream.read().split()
    input_stream.close()
    baby_names_dict = {}
    names_list.sort()
    for name in names_list:
        if name[0] in baby_names_dict:
           baby_names_dict[name[0]] += name + " "
        else:
            baby_names_dict[name[0]] = name + " "
    return baby_names_dict
baby_names_dict = create_baby_names_dictionary('2000TopNames')
def print_baby_names(baby_names_dict):
    for key, value in baby_names_dict.items():
        print(f"{key}: {value}")

print_baby_names(baby_names_dict)