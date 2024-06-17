filename = 'mand341.txt'
def print_contents(filename):
    input_stream = open(filename, 'r')
    content = input_stream.read()
    print(content)
    input_stream.close
def write_timetable(number, filename):
    output_file = open(filename, "w")
    counter = 1
    multiplied_result_list = []
    while counter < 13:
        result = counter * number
        multiplied_result_list.append(result)
        counter += 1
    counter = 1
    for result in multiplied_result_list:
        output_file.write(str(number) + " * " + str(counter) + " = " + str(result) + "\n")
        counter += 1
    output_file.close()











write_timetable(2, filename)
print_contents(filename)