text = "The quick brown fox jumps over the lazy dog"

def word_analysis(text):
    text = text.lower()
    word_list = text.split()
    dictionary = {}
    for word in word_list:
       if word[0] in dictionary:
           dictionary[word[0]] += 1
       else:
           dictionary[word[0]] = 1
    return dictionary



word_analysis_dict = word_analysis(text)
for key in sorted(word_analysis_dict):
    print(key, word_analysis_dict[key])