
def write_reversed_file(filename):
    input_stream = open(filename, "r")
    # if want to remove the newline character at the end on line 5 use .strip() at the end
    contents = input_stream.read()
    input_stream.close()
    reversed_contents = contents[::-1]
    ouput_stream = open("output.txt", "w")
    output_stream.write(reversed_contents)
    output_stream.close()

def print_contents(filename):
    input_stream = open(filename, "r")
    contents = input_stream.read()
    input_stream.close()
    print(contents)

write_reversed_file("words2.txt")
print_contents('output.txt')