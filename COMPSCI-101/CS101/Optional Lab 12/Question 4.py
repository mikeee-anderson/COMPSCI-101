def sort_tuple(a_tuple):
    a_tuple = list(a_tuple)
    a_tuple.sort()
    a_tuple = tuple(a_tuple)
    return a_tuple


print(sort_tuple((5,3,26,8,0)))