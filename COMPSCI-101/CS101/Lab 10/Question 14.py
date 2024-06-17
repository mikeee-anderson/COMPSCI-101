def get_pell_number(n):
    total = 0
    for i in range(n):
        total += i
    return total



def get_pell_number(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        pell_minus_1 = 1  # Pell(1)
        pell_minus_2 = 0  # Pell(0)
        for _ in range(2, n + 1):
            pell = 2 * pell_minus_1 + pell_minus_2
            pell_minus_2, pell_minus_1 = pell_minus_1, pell
        return pell