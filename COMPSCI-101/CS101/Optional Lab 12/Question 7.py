tuple1 = (5, 6, 2, 1, 3)
tuple2 = (3, 8, 9, 6, 7)
def get_sorted_in_parallel(tuple1, tuple2):
    paired_tuples = []
    for i in range(len(tuple1)):
        paired_tuples.append((tuple1[i], tuple2[i]))
    paired_tuples.sort()

    sorted_tuple1 = []
    sorted_tuple2 = []
    for pair in paired_tuples:
        sorted_tuple1.append(pair[0])
        sorted_tuple2.append(pair[1])
    sorted_tuple1 = tuple(sorted_tuple1)
    sorted_tuple2 = tuple(sorted_tuple2)
    return sorted_tuple1, sorted_tuple2










tuple3, tuple4 = get_sorted_in_parallel(tuple1, tuple2)
print(tuple1, "-", tuple2)




















print(tuple3, "-", tuple4)