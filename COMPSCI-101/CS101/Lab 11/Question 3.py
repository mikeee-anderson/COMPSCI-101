currency_list = ["Pound Sterling", "US Dollars", "Euros", "Canadian Dollars", "Australian Dollars", "Singaporean Dollars", "Japanese Yen"]
rate_list = [0.52, 0.62, 0.58, 0.84, 0.92, 0.84, 84.43]

def print_menu(currency_list, rate_list):
    print("Select an operation:")
    print(f"Enter 1 to exchange NZ Dollars to Pound Sterling (1 NZD = {rate_list[0]} {currency_list[0]})")
    print(f"Enter 2 to exchange NZ Dollars to US Dollars (1 NZD = {rate_list[1]} {currency_list[1]})")
    print(f"Enter 3 to exchange NZ Dollars to Euros (1 NZD = {rate_list[2]} {currency_list[2]})")
    print(f"Enter 4 to exchange NZ Dollars to Canadian Dollars (1 NZD = {rate_list[3]} {currency_list[3]})")
    print(f"Enter 5 to exchange NZ Dollars to Australian Dollars (1 NZD = {rate_list[4]} {currency_list[4]})")
    print(f"Enter 6 to exchange NZ Dollars to Singaporean Dollars (1 NZD = {rate_list[5]} {currency_list[5]})")
    print(f"Enter 7 to exchange NZ Dollars to Japanese Yen (1 NZD = {rate_list[6]} {currency_list[6]})")
    print("Enter 0 to exit the currency converter")
print_menu(currency_list, rate_list)