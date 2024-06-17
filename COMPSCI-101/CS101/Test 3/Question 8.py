
def extract_consonants(data):
    consonants = "bcdfghjklmnpqrstvwxyz"
    consonants_count = []
    for i in range(len(data)):
        if data[i] not in consonants_count:
            if data[i] in consonants:
                consonants_count.append(data[i])
    consonants_count.sort()
    consonants_count = tuple(consonants_count)
    return consonants_count


data = extract_consonants("edbca")
print(data)