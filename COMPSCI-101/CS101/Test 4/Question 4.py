def print_diagonal(number_of_lines):
    counter = 0
    spacer = " "
    while counter < number_of_lines:
        if counter == 0:
            print("x")
            counter += 1
        else:
            print(spacer + "x")
            spacer += " "
            counter += 1






print_diagonal(4)