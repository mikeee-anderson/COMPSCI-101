int_tuple = (5, 4, 3, 2, 1, 0)
factor = 2
def get_multiples_tuple(int_tuple, factor):
    new_list = []
    for number in int_tuple:
        if number % factor == 0:
            new_list.append(number)
    new_list.sort()
    new_list = tuple(new_list)
    return new_list


multiples = get_multiples_tuple(int_tuple, factor)
print(f"{multiples} are multiples of {factor}.")
print(f"{multiples} is of type {type(multiples)}.")