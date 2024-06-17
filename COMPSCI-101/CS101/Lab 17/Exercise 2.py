def create_2d_list(word):
    result = []
    for i in range(len(word)):
        sub_list = []
        for char in word:
            sub_list.append(char)
        result.append(sub_list)
    return result
print(create_2d_list('cat'))