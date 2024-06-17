radio_telephone_dict = {'B': 'Bravo', 'U': 'Uniform', 'M': 'Mike', 'S': 'Sierra', 'G': 'Golf', 'E': 'Echo', 'N': 'November', 'L': 'Lima', 'X': 'X-ray', 'D': 'Delta', 'W': 'Whiskey', 'V': 'Victor', 'Z': 'Zulu', 'F': 'Foxtrot', 'K': 'Kilo', 'O': 'Oscar', 'R': 'Romeo', 'A': 'Alpha', 'Q': 'Quebec', 'Y': 'Yankee', 'H': 'Hotel', 'J': 'Juliett', 'T': 'Tango', 'P': 'Papa', 'I': 'India', 'C': 'Charlie'}
def display_translation(word, radio_telephone_dictionary):
    for key in word:
        key = key.upper()
        word = radio_telephone_dictionary[key]
        print(word, end=" ")

display_translation('aeroplane', radio_telephone_dict)