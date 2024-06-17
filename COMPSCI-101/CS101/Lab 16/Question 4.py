sentence = 'ann met an ant'
def count_word_occurrences(sentence):
    word_list = sentence.split()
    word_dictionary = {}
    for word in word_list:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1
    return word_dictionary



word_counts_dict = count_word_occurrences(sentence)
for key in sorted(word_counts_dict):
    print(key, word_counts_dict[key])