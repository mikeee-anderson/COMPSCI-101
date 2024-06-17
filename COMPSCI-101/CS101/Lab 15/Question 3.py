text = "The quick brown fox jumps over the lazy dog"
def word_length_analysis(text):
    word_list = text.split()
    dictionary ={}
    for word in word_list:
        if len(word) in dictionary:
            dictionary[len(word)] += 1
        else:
            dictionary[len(word)] = 1
    return dictionary
        # len(word) : no. of words

word_length_dict = word_length_analysis(text)
for key in sorted(word_length_dict):
    print(f"Word Length: {key}, Number of Words: {word_length_dict[key]}")