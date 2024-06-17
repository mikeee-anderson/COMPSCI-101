words_list = [['fish', 'barrel', 'like'], ['shooting'], ['sand', 'bank'], ['apple', 'orange']]

def get_2d_list_of_vowels_count(list_of_lists):
    vowels = "AEIOUaeiou"
    new_list_of_lists = []
    for list_ in list_of_lists:
        new_list = []
        for word in list_:
            vowel_count = 0
            for i in range(len(word)):
                if word[i] in vowels:
                    vowel_count += 1
            new_list.append(vowel_count)
        new_list_of_lists.append(new_list)
    return new_list_of_lists





print(get_2d_list_of_vowels_count(words_list))