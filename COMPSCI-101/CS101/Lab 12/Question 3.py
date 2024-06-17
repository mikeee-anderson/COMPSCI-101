word_list = ['fish', 'barrel', 'like', 'noon', 'sand', 'bank']
def get_string_length_tuples(words_list):
    tuple1 = ()
    new_list = []
    for word in words_list:
        length = len(word)
        tuple1 = (word, length)
        new_list += [tuple1]
    tuple(new_list)
    return new_list

result = get_string_length_tuples(word_list)

print(result)

