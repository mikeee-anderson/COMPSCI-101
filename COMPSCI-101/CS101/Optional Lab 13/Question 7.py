sentence = "cat dog zebra cow"

def write_secret_sentence(sentence):
    vowels = 'aeiouAEIOU'
    altered_sentence = ""
    for char in sentence:
        if char in vowels:
            altered_sentence += "*"
        else:
            altered_sentence += char
    output_stream = open("mand341.txt", "w")
    output_stream.write(altered_sentence)
    output_stream.close()


def print_content(filename):
    input_file = open(filename, 'r')
    lines = input_file.readlines()
    input_file.close()
    for index in range(len(lines)):
        lines[index] = lines[index].strip()
    for line in lines:
        print(line)
    print(f'{len(lines)} line(s) read.')


write_secret_sentence(sentence)
print_content('mand341.txt')