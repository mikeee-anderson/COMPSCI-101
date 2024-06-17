def print_key_values_in_order(dict1):
    key_list = list(dict1.keys())
    key_list.sort()
    for key in key_list:
        value_list = dict1[key]
        value_list.sort()
        print(key, value_list)

def read_and_build_dict(filename):
    input_file = open(filename, "r")
    ceo = input_file.readline().strip().split(",")
    manager = input_file.readline().strip().split(",")
    sales = input_file.readline().strip().split(",")
    input_file.close()
    company_dict = {"CEO": ceo, "Manager": manager, "Sales": sales}
    return company_dict








a_dict = read_and_build_dict('company.txt')
print_key_values_in_order(a_dict)