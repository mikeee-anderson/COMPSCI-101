def get_polygonal_numbers(sides, terms):
    counter = 1
    numbers = []
    while counter <= terms:
        value = ((sides - 2) * counter ** 2 - (sides - 4) * counter) / 2
        numbers.append(int(value))
        counter += 1
    return numbers









print(f"First 5 triangular numbers are: {get_polygonal_numbers(4, 6)}")