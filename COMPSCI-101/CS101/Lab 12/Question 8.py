word_list = ['fish', 'barrel', 'like', 'noon', 'sand', 'bank']

def get_palindromes(words_list):
    palindrome_list = []
    normal_list = []
    list1 = []
    for word in words_list:
        if word == word[::-1]:
            palindrome_list += [word]
        else:
            normal_list += [word]
    list1 = [palindrome_list] + [normal_list]

    return tuple(list1)

result = get_palindromes(word_list)
print(result)




