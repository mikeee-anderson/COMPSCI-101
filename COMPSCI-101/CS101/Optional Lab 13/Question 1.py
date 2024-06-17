filename = "numbers.txt"
def read_and_count_multiples(filename, number):
    input_stream = open(filename, "r")
    numbers_list = input_stream.read().split()
    input_stream.close()
    count = 0
    for n in numbers_list:
        n = int(n)
        if n % number == 0:
            count += 1
    return count

print(read_and_count_multiples('numbers.txt', 5))