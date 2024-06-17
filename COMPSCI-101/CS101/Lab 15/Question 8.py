filename = "Inventory1.txt"


def get_inventory(filename):
    input_stream = open(filename, "r")
    lines = input_stream.readlines()
    input_stream.close()
    inventory = {}
    for line in lines[1:]:
        parts = line.split('\t')
        parts = [part.strip() for part in parts if part.strip()]
        if len(parts) == 2:
            item, price = parts
            inventory[item] = float(price)
    return inventory


def get_inventory(filename):
    # Open the file in read mode
    input_stream = open(filename, "r")

    # Read all lines from the file
    lines = input_stream.readlines()

    # Close the file
    input_stream.close()

    # Initialize an empty dictionary to store item-price pairs
    inventory = {}

    # Iterate over each line, skipping the first (header) line
    for line in lines[1:]:
        # Split the line into parts based on tab character(s)
        parts = line.split('\t')

        # Strip each part and remove empty strings
        cleaned_parts = []
        for part in parts:
            stripped_part = part.strip()
            if stripped_part:
                cleaned_parts.append(stripped_part)

        # Ensure that the cleaned parts resulted in exactly two parts
        if len(cleaned_parts) == 2:
            item, price = cleaned_parts
            inventory[item] = float(price)

    return inventory

inventory = get_inventory(filename)
for item in sorted(inventory):
    print(f"{item} => ${inventory[item]}")