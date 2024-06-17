def print_mirrored_right_angle_pattern(number_of_rows):
    for i in range(1, number_of_rows + 1):
        # Print leading spaces
        for j in range(number_of_rows - i):
            print(" ", end="")
        # Print descending numbers
        for j in range(i, 0, -1):
            print(j, end="")
        # Move to the next line
        print()
