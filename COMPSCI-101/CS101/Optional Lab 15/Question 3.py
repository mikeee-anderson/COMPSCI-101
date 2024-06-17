words_list = ['to', 'make', 'the', 'best', 'use', 'of', 'information', 'technology', 'schools', 'need', 'a', 'workable', 'plan', 'to', 'fully', 'integrate', 'it', 'into', 'all', 'aspects', 'of', 'the', 'curriculum', 'so', 'students', 'are', 'taught', 'how', 'why', 'and', 'when', 'to', 'use', 'technology', 'to', 'further', 'enhance', 'their', 'learning']
def create_vowels_dictionary(words_list):
    vowels = "aeiou"
    vowels_dict = {"a":[], "e":[], "i":[], "o":[], "u":[]}
    words_list.sort()
    for word in words_list:
        if word[0] == "a":
            if word not in vowels_dict["a"]:
                vowels_dict["a"].append(word)
        elif word[0] == "e":
            if word not in vowels_dict["e"]:
                vowels_dict["e"].append(word)
        elif word[0] == "i":
            if word not in vowels_dict["i"]:
                vowels_dict["i"].append(word)
        elif word[0] == "o":
            if word not in vowels_dict["o"]:
                vowels_dict["o"].append(word)
        elif word[0] == "u":
            if word not in vowels_dict["u"]:
                vowels_dict["u"].append(word)
    return vowels_dict





a_dict = create_vowels_dictionary(words_list)
for key in a_dict:
    print(key, a_dict[key])