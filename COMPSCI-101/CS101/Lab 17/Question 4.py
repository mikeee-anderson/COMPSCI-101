def print_number_triangle(number_of_rows):
    current_number = 1
    for row in range(1, number_of_rows + 1):
        for col in range(row):
            # Print the number formatted as two digits
            print(f"{current_number:02}", end=" ")
            current_number += 1
        # Print a new line after each row
        print()


print_number_triangle(5)