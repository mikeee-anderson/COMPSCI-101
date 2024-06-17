line_of_prices = input("Enter a list of apartment prices: ")
line_of_bedrooms = input("Enter a list of numbers of bedrooms: ")

price_list = line_of_prices.split(',')
bedroom_list = line_of_bedrooms.split(',')


lower_bedroom = 0
lower_count = 0
upper_bedroom = 0
upper_count = 0
index = 0
for price in price_list:
    price = int(price)
    if int(bedroom_list[index]) == 1 or int(bedroom_list[index]) == 2:
        lower_bedroom += price
        lower_count += 1
    elif int(bedroom_list[index]) == 3 or int(bedroom_list[index]) == 4:
        upper_bedroom += price
        upper_count += 1
    index += 1


if lower_count < 1:
    print("There is no apartment with 1 or 2 bedrooms in the list.")
else:
    lower_average = round(lower_bedroom / lower_count)
    print(f"The average price for apartments with 1 or 2 bedrooms is ${lower_average}.")
if upper_count < 1:
    print("There is no apartment with 3 or 4 bedrooms in the list.")
else:
    upper_average = round(upper_bedroom / upper_count)
    print(f"The average price for apartments with 3 or 4 bedrooms is ${upper_average}.")

