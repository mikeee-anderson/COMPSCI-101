
#    print(f"Word Length: {key}, Number of Words: {word_length_dict[key]}")
def translate_english_maori(maori_dictionary, word):
    if word not in maori_dictionary:
        print("Sorry that word doesn't exist in Maori!")
    else:
        print(f"'{word}' is translated into '{maori_dictionary[word]}'.")





translate_english_maori(a_dict, 'house')