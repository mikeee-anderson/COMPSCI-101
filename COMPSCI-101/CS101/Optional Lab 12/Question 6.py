
def analyze_text(text):
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"
    text = text.lower()
    vowel_collection = []
    consonant_collection = []
    for i in range(len(text)):
        if text[i] in vowels:
            if text[i] not in vowel_collection:
                    vowel_collection.append(text[i])
        if text[i] in consonants:
            if text[i] not in consonant_collection:
                consonant_collection.append(text[i])
    vowel_collection.sort()
    consonant_collection.sort()
    vowel_collection = tuple(vowel_collection)
    consonant_collection = tuple(consonant_collection)
    combined_list = [vowel_collection, consonant_collection]
    return combined_list










text = "Hello world!"
print("Text analysis:", analyze_text(text))