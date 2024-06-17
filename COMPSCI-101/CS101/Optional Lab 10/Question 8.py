password = "Damir 1234?"
def is_valid_password(password_string):
    uppercase_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase_alphabet = "abcdefghijklmnopqrstuvwxyz"
    numbers = "0123456789"
    symbols = "!&*$#<>?"
    if len(password_string) < 8:
        return False

    numerical_digit = 0
    symbol = 0
    lowercase = 0
    uppercase = 0
    error = 0
    for i in range(len(password_string)):
        if password_string[i] not in uppercase_alphabet and password_string[i] not in lowercase_alphabet and password_string[i] not in numbers and password_string[i] not in symbols:
            error += 1
        if password_string[0] in uppercase_alphabet:
            uppercase += 1
        if password_string[i] in numbers:
            numerical_digit += 1
        if password_string[i] in symbols:
            symbol += 1
        if password_string[i] in lowercase_alphabet:
            lowercase += 1
    if numerical_digit == 0 or symbol == 0 or lowercase_alphabet == 0 or uppercase == 0 or error > 0:
        return False
    else:
        return True







print(password, "is valid:", is_valid_password(password))
