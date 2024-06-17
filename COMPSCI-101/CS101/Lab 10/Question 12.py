def get_list_of_four_letter_words(words_list):
    new_list = []
    for word in words_list:
        word = word.lower()
        if len(word) == 4:
            new_list.append(word)
    return new_list
