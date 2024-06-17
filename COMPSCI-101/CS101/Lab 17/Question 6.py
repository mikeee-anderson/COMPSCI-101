number = 12345
def digital_root(number):
    while number >= 10:
        sum_of_digits = 0
        while number > 0:
            sum_of_digits += number % 10
            number //= 10
        number = sum_of_digits
    return number





print(f"Digital Root of {number} = {digital_root(number)}")
print(f"Function return type = {type(digital_root(number))}")