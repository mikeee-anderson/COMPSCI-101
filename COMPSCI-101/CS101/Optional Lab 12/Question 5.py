secret = [5, 6, 7, 8]
guess = [1, 2, 3, 4]
def bulls_and_cows(guess, secret):
    bulls = 0
    cows = 0
    for i in range(len(secret)):
        if guess[i] in secret:
            cows += 1
        if guess[i] == secret[i]:
            bulls += 1
            cows -= 1
    result = (bulls, cows)
    return result



result_tuple = bulls_and_cows(guess, secret)
print(type(result_tuple))
print("Bulls:", result_tuple[0], "Cows:", result_tuple[1])