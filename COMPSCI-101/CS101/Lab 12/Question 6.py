
a_list = [2, -4, 99, 12, 56, 25]
def get_min_median_max(numbers):
    small = min(numbers)
    large = max(numbers)
    numbers.sort()
    index = int(len(numbers) / 2)
    if len(numbers) % 2 != 0:
        tuple1 = (small, numbers[index], large)
    else:
        value1 = int(index - 1)
        value2 = index
        median = (numbers[value1] + numbers[value2]) / 2
        tuple1 = (small, median, large)
    return tuple1

print(get_min_median_max(a_list))