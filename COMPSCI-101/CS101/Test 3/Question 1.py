
def get_acceptable_input(acceptable_words):
    user = input("Enter a word: ")
    while user not in acceptable_words:
        user = input("Enter a word: ")
    return user


chosen = get_acceptable_input(["WORDS", "TEST", "EXAM", "QUESTION"])
print(chosen)