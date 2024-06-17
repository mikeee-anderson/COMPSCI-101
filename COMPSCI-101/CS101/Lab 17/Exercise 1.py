def create_2d_square_numbers_list(n):
    result = []
    for i in range(1, n + 1):
        sub_list = []
        for j in range(1, n + 1):
            sub_list.append(i)
        result.append(sub_list)
    return result
print(create_2d_square_numbers_list(5))