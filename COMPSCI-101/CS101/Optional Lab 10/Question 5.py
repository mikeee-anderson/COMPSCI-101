temperature_list = [24.3, 25.9, 22.8, 26.4, 25.4, 25.7, 28.9, 27.6]
def calculate_average_spring_temperature(temperature_list):
    counter = 0
    total = 0
    for temperature in temperature_list:
        if temperature > 26:
            break
        else:
            total += temperature
            counter += 1
    if counter == 0:
        average = 0.0
    else:
        average = round(total / counter, 2)
    return average






print(f"Average spring temperature: {calculate_average_spring_temperature(temperature_list)}")