data = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
goal = 10

def combinations(data, goal):
    valid_combinations = []
    for i in range(len(data)):
        number1 = data[i]
        for n in range(i + 1, len(data)):
            number2 = data[n]
            if number1 + number2 == goal:
                valid = [number1, number2]
                valid.sort()
                valid = tuple(valid)
                if valid not in valid_combinations:
                    valid_combinations.append(valid)
    return valid_combinations







print(combinations(data, goal))