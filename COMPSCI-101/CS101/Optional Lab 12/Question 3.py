tuple1 = ("A", "B")
tuple2 = ("C", "D")
def join_tuples(tuple1, tuple2):
    combined = []
    for i in range(len(tuple1)):
        combination = tuple1[i] + tuple2[i]
        combined.append(combination)
    combined = tuple(combined)
    return combined




result = join_tuples(tuple1, tuple2)
print(f"Tuple result: {result}")
print(f"Checking return type: {type(result)}")