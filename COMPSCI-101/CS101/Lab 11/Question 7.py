def main():
    currency_list = ["Pound Sterling", "US Dollars", "Euros", "Canadian Dollars",
                     "Australian Dollars", "Singaporean Dollars", "Japanese Yen"]
    rate_list = [0.52, 0.62, 0.58, 0.84, 0.92, 0.84, 84.43]
    #Complete the main() function
    print_banner()
    print(" ")
    print_menu(currency_list, rate_list)
    print(" ")
    perform_currency_exchange(currency_list, rate_list)
    print(" ")
    print_exit_message()


def print_banner():
    print("**********************")
    print("*A Currency Converter*")
    print("**********************")

def print_menu(currency_list, rate_list):
    print("Select an operation:")
    for i in range(len(currency_list)):
        number = i + 1
        print(f"Enter {number} to exchange NZ Dollars to {currency_list[i]}"
        f" (1 NZD = {rate_list[i]} {currency_list[i]})")
    print("Enter 0 to exit the currency converter")


def print_exit_message():
    print("Exiting the currency converter...")
    print("Have a good day!")

def perform_currency_exchange(currency_list, rate_list):
    selection = int(input("Enter your selection: "))
    while selection < 0 or selection > 7:
        print("Invalid selection!")
        selection = int(input("Enter your selection: "))

    nz_amount = float(input("Enter the amount of NZ dollars you want to convert: "))
    if selection == 6:
        converted_amount = round(nz_amount * rate_list[selection])
    else:
        converted_amount = round(nz_amount * rate_list[selection], 2)
        print(f"${nz_amount} NZ dollars = ${converted_amount} {currency_list[selection]}")
        selection = int(input("Enter your selection: "))


main()

