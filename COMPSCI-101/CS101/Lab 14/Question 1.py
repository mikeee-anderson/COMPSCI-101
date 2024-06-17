
def write_names(names):
    output_stream = open("output.txt", "w")
    for name in names:
        output_stream.write(name + "\n")
    output_stream.close()

def print_contents(filename):
    input_stream = open(filename, "r")
    contents = input_stream.read()
    input_stream.close()
    print(contents)
write_names(['peter', 'dick', 'anna'])

print_contents('output.txt')