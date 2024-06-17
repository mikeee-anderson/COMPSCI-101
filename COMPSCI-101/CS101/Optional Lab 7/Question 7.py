amount = input("Enter an amount: ")

while len(amount) < 4:
    amount = input("Enter an amount: ")

while len(amount) == 4:
    if "." not in amount:
        amount = input("Enter an amount: ")
    if amount[amount.find(".") - 1].isdigit() == False:
        amount = input("Enter an amount: ")
    if amount[amount.find(".") - 1].isdigit() == False:
        amount = input("Enter an amount: ")
    if (amount[amount.find(".") + 1].isdigit() == False) and (amount[amount.find(".") + 2].isdigit() == False):
        amount = input("Enter an amount: ")

print(f"{amount} is a valid amount.")