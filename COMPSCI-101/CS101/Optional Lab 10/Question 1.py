
def print_palindromes(words_list):
    for word in words_list:

        if word[0::] == word[::-1]:
            print(f"{word} is a palindrome.")









print_palindromes(['anna', 'two', 'civic', 'here', 'five', 'hanah', 'seven', 'eight', 'nine', 'ten'])