def replace_a_value (a_tuple, index, new_value):
    a_list = list(a_tuple)
    a_list[index] = new_value
    a_tuple = tuple(a_list)
    return a_tuple

tuple1 = ('one', 'two', 'three')
tuple1 = replace_a_value(tuple1, 2, 'SIX')
print(tuple1)