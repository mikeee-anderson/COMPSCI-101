phrase = input("Enter a phrase: ")
phrase = phrase.upper()
words = phrase.split()
acronym = ""
for word in words:
    acronym += word[0]

print(acronym)

