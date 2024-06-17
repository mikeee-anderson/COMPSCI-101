


def get_list_of_countries(filename):
    input_file = open(filename, "r")
    content = input_file.read().split()
    return content

def create_country_code_dictionary(lines_list):
    country_code_dict = {}
    for line in lines_list:
        country = line.split(":")
        country_code_dict[country[0]] = country[1]
    return country_code_dict




lines = get_list_of_countries('countries.txt')
countries_dictionary = create_country_code_dictionary(lines )
for key in sorted(countries_dictionary.keys()):
    print(key, countries_dictionary[key])