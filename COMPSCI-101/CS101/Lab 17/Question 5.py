filename = "Data1.txt"



def get_line_averages(filename):
    input_stream = open(filename, "r")
    contents = input_stream.read().split("\n")
    input_stream.close()
    line_averages = []
    for s in contents:
        line = s.split()
        sum_total = 0
        number_of_numbers = 0
        for number in line:
            number = float(number)
            sum_total += number
            number_of_numbers += 1
        if number_of_numbers != 0:
            average = round(sum_total / number_of_numbers, 2)
            line_averages.append(average)
    return line_averages


line_averages = get_line_averages(filename)
print("Line averages:", line_averages)
print("Checking return type:", type(line_averages))

