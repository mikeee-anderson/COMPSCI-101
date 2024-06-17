sentence = input("Enter a sentence: ")
vowel = "AEIOUaeiou"

index = 0
consonants=[]
while index < len(sentence):
    if sentence[index] not in vowel:
        consonants = consonants + [index]
    index += 1
counter = 0

print("New sentence: ", end= '')
while counter < len(consonants):
    print(sentence[consonants[counter]], end= '')
    counter += 1

