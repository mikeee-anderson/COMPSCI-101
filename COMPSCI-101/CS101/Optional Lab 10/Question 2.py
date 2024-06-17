def count_decimal_places(number):
    decimal_places = 0
    while number % 1 != 0:
        decimal_places += 1
        number = number * 10
    return decimal_places





print(count_decimal_places(1.12345))