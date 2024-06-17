def print_contents(filename):
    input_file = open(filename, 'r')
    content = input_file.read()
    input_file.close()
    print(content)
def write_double_numbers(filename, numbers):
    output_file = open(filename, "w")
    doubles_list = []
    for number in numbers:
        result = number * 2
        doubles_list.append(result)
    for double in doubles_list:
        output_file.write(str(double) + "\n")
    output_file.close()






write_double_numbers('mand341.txt', [1, 3, 5, 7, 9])
print_contents('mand341.txt')