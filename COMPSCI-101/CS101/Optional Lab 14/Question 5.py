def print_contents(filename):
    input_file = open(filename, 'r')
    content = input_file.read()
    input_file.close()
    print(content)

def write_evens_odds(filename, int_tuple):
    output_file = open(filename, "w")
    evens = []
    int_tuple = list(int_tuple)
    int_tuple.sort()
    odds = []
    for number in int_tuple:
        if number % 2 == 0:
            if str(number) not in evens:
                evens.append(str(number))
        else:
            if str(number) not in odds:
                odds.append(str(number))
    seperator = ", "
    output_file.write("Even numbers: " + seperator.join(evens) + "\n")
    output_file.write("Odd numbers: " + seperator.join(odds) + "\n")
    output_file.close()


int_tuple = (2, 21, 14, -5, 4, 3, -2, -9, 17, 7, 23, -2,
             -7, 18, -3, -7, 8, -1, 8, -10, -4, 2, -10, -2,
             15, -5, -2, 12, 14, -2, -3, 14, -10, 22, 5,
             -7, 6)
filename = 'mand341.txt'
write_evens_odds(filename, int_tuple)
print_contents(filename)