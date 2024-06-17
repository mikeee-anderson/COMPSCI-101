data = [0, 1, 2, 3, 4, 5, -5, -4, -3, -2, -1, 0]
def partition(data):
    odds = []
    zero = []
    evens = []
    for number in data[:]:
        if number < 0:
            data.remove(number)
    print(data)
    for number in data[:]:
        if number % 2 == 0 and number != 0:
            evens.append(number)
        elif number == 0:
            zero.append(number)
        else:
            odds.append(number)
    data[:] = odds + zero + evens


partition(data)
print(data)

