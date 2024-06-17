filename = "Data2.txt"

def get_line_totals(filename):
    input_file = open(filename, "r")
    list_of_lines = input_file.read().split("\n")
    digit_list = []
    for line in list_of_lines:
        parts = line.split()
        total = 0
        for part in parts:
            if part.isalpha():
                total += 0
            elif part.isdigit():
                part = int(part)
                total += part
            else:
                part = float(part)
                total += part
        total = round(total, 2)
        digit_list.append(total)

    return digit_list










    print(list_of_lines)

print(get_line_totals(filename))