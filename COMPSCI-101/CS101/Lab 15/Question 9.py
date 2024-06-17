inventory = {'Snickers Bar': 0.99, 'Mars Bar': 0.99, 'Crunchie Bar': 0.99, 'Pepsi 355ml Can': 1.15, 'Pepsi Max 355ml Can': 1.15, 'Coke 355ml Can': 1.2, 'Coke Zero 355ml Can': 1.2}
order = [("Snickers Bar", 3), ("Mars Bar", 2), ("Pepsi Max 355ml Can", 5)]
def calculate_order_total(order, inventory):
    total_cost = 0
    for item in order:
        item = list(item)
        amount = inventory[item[0]] * item[1]
        total_cost += amount
    return total_cost



print(f"The order total is ${round(calculate_order_total(order, inventory), 2)}")
