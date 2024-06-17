def load_names(filename):
    input_file = open(filename, "r")
    # strip() gets rid of excess blank element in the list
    contents = input_file.read().strip()
    input_file.close()
    names = contents.split("\n")\
    return names

values = load_names("names.txt")
print(values)