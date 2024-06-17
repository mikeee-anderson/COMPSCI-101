def print_contents(filename):
    input_file = open(filename, 'r')
    content = input_file.read()
    input_file.close()
    print(content)


def write_triangle(filename, num_rows):
    output_file = open(filename, "w")
    if num_rows < 1:
        output_file.write("Invalid number of rows!" + "\n")
    else:
        counter = 1
        while counter < num_rows + 1:
            output_file.write("*" * counter + "\n")
            counter += 1
    output_file.close()





write_triangle('mand341.txt', 3)
print_contents('mand341.txt')