text = "The quick brown fox jumps over the lazy dog"
text = text.lower()
def get_letter_frequency(text):
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

letter_freq_list = get_letter_frequency(text)
print(f"Letter Frequencies: {letter_freq_list}")


