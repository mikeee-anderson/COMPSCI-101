bit_string = "1100000"

def even_parity(bit_string):
    count = 0
    for i in range(len(bit_string)):
        if bit_string[i] == '1':
            count += 1
    if count % 2 == 0:
        bit_string += '0'
        return bit_string
    else:
        bit_string += '1'
        return bit_string



print(f"{bit_string} --Even Parity--> {even_parity(bit_string)}")