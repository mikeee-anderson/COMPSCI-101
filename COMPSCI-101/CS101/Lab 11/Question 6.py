def perform_currency_exchange(currency_list, rate_list):
    selection = int(input("Enter your selection: "))
    while selection != 0:
        selection -= 1
        nz_amount = float(input("Enter the amount of NZ dollars you want to convert: "))
        if selection == 6:
            converted_amount = round(nz_amount * rate_list[selection])
        else:
            converted_amount = round(nz_amount * rate_list[selection], 2)
        print(f"${nz_amount} NZ dollars = ${converted_amount} {currency_list[selection]}")
        selection = int(input("Enter your selection: "))

