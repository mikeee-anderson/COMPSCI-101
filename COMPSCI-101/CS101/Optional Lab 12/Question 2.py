def get_date():
    day = input("Enter a day: ")
    month = input("Enter a month: ")
    year = input("Enter a year: ")
    tuple1 = (day, month, year)
    return tuple1


tuple_date = get_date()
print(tuple_date)
print(type(tuple_date))