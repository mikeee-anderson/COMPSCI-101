text = "The quick brown fox jumps over the lazy dog"



def get_letter_frequency(text):
    text = text.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    list1 = []
    for letter in alphabet:
        counter = 0
        total = 0
        while counter < len(text):
            if text[counter] == letter:
                total += 1
            counter += 1
        tuple1 = (letter, total)
        list1 += [tuple1]
    return list1

def draw_letter_frequency_chart(letter_freq_list):
    for letter in letter_freq_list:
        list(letter)
        if letter[1] > 0:
            print(f"{letter[0]}|{'#' * letter[1]}{letter[1]}")


letter_freq_list = get_letter_frequency(text)
print("Letter Frequencies:")
draw_letter_frequency_chart(letter_freq_list)