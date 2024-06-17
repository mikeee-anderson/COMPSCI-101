text = "The quick brown fox jumps over the lazy dog."


def get_character_classification_dict(text):
    char_dictionary = {}
    digit = 0
    letter = 0
    others = 0
    for char in text:
        if char.isdigit():
            digit += 1
        elif char.isalpha():
            letter += 1
        else:
            others += 1
    char_dictionary["digits"] = digit
    char_dictionary["letters"] = letter
    char_dictionary["other"] = others
    return char_dictionary







char_classifier_dict = get_character_classification_dict(text)
for key in sorted(char_classifier_dict):
    print(f"{key}: {char_classifier_dict[key]}")