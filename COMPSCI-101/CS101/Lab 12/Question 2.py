numbers = [4, -5, 2, 8, 0, -4, ]
def get_sum_evens_odds(numbers_list):
    odd_total = 0
    even_total = 0
    for numb in numbers_list:
        if numb % 2 == 0:
            even_total += numb
        else:
            odd_total += numb
    tuple1 = (even_total, odd_total)
    return tuple1


print(get_sum_evens_odds(numbers))
