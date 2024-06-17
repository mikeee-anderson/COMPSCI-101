first_word = input("Please enter the first 6 letter word: ")
second_word = input("Please enter the second 6 letter word: ")

pokemon_name = first_word[0:4] + second_word[3:]

print(f"New Pokemon name: {pokemon_name}")


