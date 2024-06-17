number = input("Enter a number (blank to exit): ")
data = []
while number != "":
    number = int(number)
    data += [number]
    number = input("Enter a number (blank to exit): ")

data = sorted(data)
print(f"Data: {data}")

if len(data) % 2 != 0:
    median = data[round((len(data) // 2))]
    print(f"Median: {median}")
else:
    middle_values = data[(len(data) // 2) - 1] + data[(len(data) // 2)]
    median = middle_values / 2
    print(f"Median: {median}")
