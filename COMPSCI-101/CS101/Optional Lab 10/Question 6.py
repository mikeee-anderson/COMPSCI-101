number_string = "21.543,35.814"
sentinel_value = 32.9908
def get_funny_average(number_string, sentinel_value):
    total = 0
    counter = 0
    start = 0
    for i in range(len(number_string)):
        if number_string[i] == ',' or i == len(number_string) - 1:
            number = float(number_string[start:i]) if i != len(number_string) - 1 else float(number_string[start:])
            if number >= sentinel_value:
                break
            if number > 0:
                total += number
                counter += 1
            start = i + 1
    if counter == 0:
        average = 0.0
    else:
        average = round(total / counter)

print("The funny average is:", get_funny_average(number_string, sentinel_value))




