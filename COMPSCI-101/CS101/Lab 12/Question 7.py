numbers = [9, 5, 1, 4, 5, 1, 7, 7]
def get_duplicates_count(numbers_list):
    list1 = []
    numbers.sort()
    for number in numbers_list:
        counter = 0
        total = 0
        while counter < len(numbers_list):
            if numbers_list[counter] == number:
                total += 1
            counter += 1
        if total > 1:
            tuple1 = (number, total)
            if tuple1 not in list1:
                list1 += [tuple1]
    tuple(list1)
    return list1


print(get_duplicates_count(numbers))