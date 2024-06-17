char_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
             'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
             'S', 'T', 'U', 'V', 'W', 'X','Y', 'Z', ' ']
morse_list = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.',
              '....','..', '.---', '-.-', '.-..', '--', '-.',
              '---', '.--.', '--.-', '.-.', '...', '-', '..-',
              '...-', '.--', '-..-','-.--', '--..', ' ']

text = input("Enter a text: ")
text = text.upper()
morse = ""
for char in text:
    morse += morse_list[char_list.index(char)]
    morse += " "
morse.strip()
print(f"The translation in Morse code is: {morse}")
