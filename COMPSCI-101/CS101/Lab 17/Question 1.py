words = ['aria', 'curb', 'cutoff', 'academic', 'aged', 'the', 'dog', 'hello']

def create_last_letter_dictionary(words_list):
    words_dict = {}
    for word in words_list:
        last_letter = word[-1]
        if last_letter not in words_dict:
            words_dict[last_letter] = []
        words_dict[last_letter].append(word)
        words_dict[last_letter].sort()
    return words_dict

words_dict = create_last_letter_dictionary(words)
for key in sorted(words_dict):
    print(f"{key}: {', '.join(words_dict[key])}")


