translations_list = ['black:mangu', 'hello:kiaora', 'house:whare', 'apple:aporo', 'tree:aroha', 'work:mana', 'red:whero']

def build_english_to_maori(translations_list):
    dictionary = {}
    for word in translations_list:
        pair = word.split(":")
        dictionary[pair[0]] = pair[1]
    return dictionary



translation_dict = build_english_to_maori(translations_list)
print(translation_dict)