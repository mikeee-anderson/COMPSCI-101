digit_list = ["-VE", "EIGHT", "SEVEN", "ZERO", "FIVE"]

def get_integer(digit_list):
    negative = False
    decimal_integer = ""
    for number in digit_list:
        if number == "-VE":
            negative = True
        elif number == "ONE":
            decimal_integer += "1"
        elif number == "TWO":
            decimal_integer += "2"
        elif number == "THREE":
            decimal_integer += "3"
        elif number == "FOUR":
            decimal_integer += "4"
        elif number == "FIVE":
            decimal_integer += "5"
        elif number == "SIX":
            decimal_integer += "6"
        elif number == "SEVEN":
            decimal_integer += "7"
        elif number == "EIGHT":
            decimal_integer += "8"
        elif number == "NINE":
            decimal_integer += "9"
        elif number == "ZERO":
            decimal_integer += "0"
    decimal_integer = int(decimal_integer)
    if negative == True:
        decimal_integer *= -1
    return decimal_integer



int_val = get_integer(digit_list)
print("The integer is:", int_val)