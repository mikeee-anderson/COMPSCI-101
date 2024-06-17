def print_content(filename):
    input_file = open(filename, 'r')
    lines = input_file.readlines()
    input_file.close()
    for index in range(len(lines)):
        lines[index] = lines[index].strip()
    for line in lines:
        print(line)
    print(f'{len(lines)} line(s) read.')

def write_secret_sentence(sentence):
    output_file = open('mand341.txt', "w")
    vowels = 'aeiouAEIOU'
    secret_sentence = ""
    for char in sentence:
        if char in vowels:
            secret_sentence += "*"
        else:
            secret_sentence += char
    output_file.write(secret_sentence +"\n")
    output_file.close()







sentence = "cat dog zebra cow"
write_secret_sentence(sentence)
print_content('mand341.txt')