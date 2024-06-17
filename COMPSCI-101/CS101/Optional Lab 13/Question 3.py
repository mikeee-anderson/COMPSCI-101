filename = "many_words1.txt"

def get_words(filename):
    input_stream = open(filename, "r")
    target_letter = input_stream.readline().strip()
    target_length = input_stream.readline().strip()
    words_list = input_stream.read().split()
    input_stream.close()
    target_length = int(target_length)
    valid_words = []
    for word in words_list:
        if word.startswith(target_letter) and len(word) == target_length:
            valid_words.append(word)
    tuple1 = (target_letter, target_length, valid_words)
    return tuple1


data_tuple = get_words(filename)
print(data_tuple[1]," letter words beginning with ",data_tuple[0],": ",data_tuple[2],sep="")