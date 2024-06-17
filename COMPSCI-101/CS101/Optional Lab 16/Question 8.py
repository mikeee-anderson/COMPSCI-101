def print_dict(a_dict):
    key_list = list(a_dict.keys())
    key_list.sort()
    for key in key_list:
        print(str(key )+ ": " + str(a_dict[key]))

def process_marks(filename):
    input_file = open(filename, "r")
    contents = input_file.read()

filename1 = "Input1.txt"
marks_dict = process_marks(filename1)
print_dict(marks_dict)