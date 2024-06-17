def carry_out_transactions(balance, transactions_tuple):
    withdrawls = 0
    deposits = 0
    for value in transactions_tuple:
        if value < 0:
            balance += value
            withdrawls += abs(value)
        else:
            balance += value
            deposits += value
    tuple1 = (balance, deposits, withdrawls)
    return tuple1






results = carry_out_transactions(5400, (100, -400, 500,
                                            -800, 600, -100, - 200, 50, 0, -200))
print("Balance $", results[0], ", deposits $", results[1],
          ", withdrawals $", results[2], sep="")
