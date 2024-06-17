
filename = "numbers1.txt"

def count_numbers(filename):
    input_file = open(filename, "r")
    contents = input_file.read()
    numbers_list = contents.split()
    negative_count = 0
    positive_count = 0
    for number in numbers_list:
        number = int(number)
        if number < 0:
            negative_count += 1
        else:
            positive_count += 1
    tuple1 = (negative_count, positive_count)
    input_file.close()
    return tuple1



counts = count_numbers(filename)
print(f"Negative number count: {counts[0]}, Non-negative number count: {counts[1]}")
print("Type:", type(counts))