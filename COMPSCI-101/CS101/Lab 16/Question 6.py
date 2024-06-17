a_dict = {53: ['bleats', 'stable', 'tables'], 34: ['angle', 'angel' ], 37: ['arcs', 'cars'], 42: ['goes']}

def get_smallest(code_dictionary):
    keys_list = list(a_dict)
    minimum_key = min(keys_list)
    target_list = code_dictionary[minimum_key]
    target_list.sort()
    return target_list[0]



print(get_smallest(a_dict))