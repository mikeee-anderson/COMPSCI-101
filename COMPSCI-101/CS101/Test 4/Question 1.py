int_tuple = (-4, -6, -2, 11, 0, 15)
def print_contents(filename):
    input_file = open(filename, 'r')
    content = input_file.read()
    input_file.close()
    print(content)

def write_positive_negative(filename, int_tuple):

    output_file = open(filename, "w")
    positive_list = []
    negative_list = []
    int_tuple = list(int_tuple)
    int_tuple.sort()
    for number in int_tuple:
        if number < 0:
            if str(number) not in negative_list:
                number = str(number)
                negative_list.append(number)
        elif number > 0:
            if str(number) not in positive_list:
                number = str(number)
                positive_list.append(number)
    seperator = ", "
    positive_number_string = seperator.join(positive_list)
    negative_number_string = seperator.join(negative_list)
    output_file.write(f"Positive numbers: {positive_number_string}" + "\n")
    output_file.write((f"Negative numbers: {negative_number_string}"))
    output_file.close()






filename = 'mand341.txt'
write_positive_negative(filename, int_tuple)
print_contents(filename)
