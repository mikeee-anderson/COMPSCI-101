def print_facing_triangles(number_of_rows):
    counter = 0
    spacer = "  "
    original = number_of_rows
    while counter < number_of_rows:
        if counter == 0:
            print("*" * number_of_rows * 2)
            counter += 1
        else:
            original -= 1
            print("*" * original + spacer + "*" * original)
            spacer += "  "
            counter += 1






print_facing_triangles(5)