def combine_and_write(list1, list2):
    output_stream = open("output.txt", "w")
    for i in range(len(list1)):
        output_stream.write(str(list1[i]) + " : " + str(list2[i]) + "\n")
    output_stream.close()


def print_contents(filename):
    input_stream = open(filename, "r")
    contents = input_stream.read()
    input_stream.close()
    print(contents)


list1 = [2, 5, 6, 8, 1]
list2 = [123, 54, 58, 106, 87, 206]
combine_and_write(list1, list2)
print_contents('output.txt')