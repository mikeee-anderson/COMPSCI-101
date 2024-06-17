
def word_analysis(word):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    score = 0
    for char in word:
        score += letters.find(char)
    tuple1 = (word, len(word), score)
    return tuple1



print(word_analysis('at'))