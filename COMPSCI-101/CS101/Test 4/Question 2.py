filename = 'mand341.txt'
nested_list = [[0, 11, 1], [12, 46]]

def write_nested_list_averages(nested_list, filename):
    output_file = open(filename, "w")
    for number_list in nested_list:
        total = 0
        count = 0
        for number in number_list:
            total += number
            count += 1
        average = round(total / count, 2)
        output_file.write(str(average) + "\n")
    output_file.close()


def print_contents(filename):
    input_stream = open(filename, 'r')
    content = input_stream.read()
    print(content)
    input_stream.close()


write_nested_list_averages(nested_list, filename)
print_contents(filename)