numbers = [12, 2, 4], [1, 12, 3, 8], [3, 4], [4]
def get_one_d_unique_list(list_of_lists):
    unique_list = []
    for list in list_of_lists:
        for number in list:
            if number not in unique_list:
                unique_list.append(number)
    unique_list.sort()
    return unique_list



print(get_one_d_unique_list(numbers))