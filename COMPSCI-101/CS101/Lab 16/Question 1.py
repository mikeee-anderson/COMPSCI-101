radio_telephone_alphabet = ('Alpha', 'Foxtrot', 'Kilo', 'Papa',  'Uniform', 'Zulu')
def create_radio_telephone_dictionary(radio_telephone_tuple):
    dictionary = {}
    for word in radio_telephone_tuple:
        dictionary[word[0]] = word
    return dictionary

radio_telephone_dict = create_radio_telephone_dictionary(radio_telephone_alphabet)
for key in sorted(radio_telephone_dict ):
    print(key, radio_telephone_dict [key])