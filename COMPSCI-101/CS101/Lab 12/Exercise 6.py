def create_tuples(list1, list2):
    list_of_tuples = []
    for i in range(len(list1)):
        tuple_pair = (list1[i], list2[i])
        list_of_tuples.append(tuple_pair)
    return list_of_tuples


list_of_tuples = create_tuples([1, 2, 3, 4], [2, 4, 6, 8])
print(list_of_tuples)