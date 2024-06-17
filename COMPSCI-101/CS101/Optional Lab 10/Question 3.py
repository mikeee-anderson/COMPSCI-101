sentence = "Happiness is when what you think what you say and what you do are in harmony"


def get_words_by_length(sentence, number_of_letters):
    list_of_words = sentence.split()
    valid_list = []
    for word in list_of_words:
        if number_of_letters == len(word):
            valid_list.append(word)
    return valid_list




word_list = get_words_by_length(sentence, 2)
print(word_list)