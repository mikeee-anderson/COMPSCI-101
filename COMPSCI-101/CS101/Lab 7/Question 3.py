sentence = input("Please enter the sentence: ")

position_1 = sentence.find("(")
position_2 = sentence.rfind(")")

if position_1 != -1 and position_2 != -1:
    new_sentence = sentence[:position_1].strip() + sentence[position_2 + 1:]
    print(f"New sentence after removal: {new_sentence}")
else:
    print("No text to remove.")
