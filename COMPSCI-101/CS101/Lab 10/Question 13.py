def get_encrypted(word, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encrypted = ""
    for char in word:
        position = alphabet.find(char)
        encrypted += key[position]
    return encrypted