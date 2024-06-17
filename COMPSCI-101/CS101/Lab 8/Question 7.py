alphabet = "abcdefghijklmnopqrstuvwxyz"
letter_counts = [0] * 26
message = input("Enter a message: ")
message = message.lower()
message = message.strip()
frequency = []
for character in message:
    if character.isalpha():
        index = ord(character) - ord('a')

        letter_counts[index] += 1

print(f"The frequency list is:  {letter_counts}")
