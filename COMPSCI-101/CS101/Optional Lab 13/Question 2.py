filename = "Data1.txt"
def get_file_total(filename):
    input_stream = open(filename, "r")
    list1 = input_stream.read().split()
    input_stream.close()
    total = 0
    for numbers in list1:
        numbers_list = numbers.split(',')
        for i in numbers_list:
            i = int(i)
            total += i
    return total





print(f"File total = {get_file_total(filename)}")