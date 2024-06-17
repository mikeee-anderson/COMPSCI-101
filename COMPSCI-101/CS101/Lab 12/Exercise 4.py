def get_statistics(numbers):
    positive_sum = 0
    positive_count = 0
    for number in numbers:
        if number > 0:
            positive_sum += number
            positive_count += 1
    if positive_count == 0:
        positive_average = 0
    else:
        positive_average = round(positive_sum / positive_count)
    return (positive_sum, positive_average)
a_list = [-2, 6, -3, -9, 20]
print(get_statistics(a_list))