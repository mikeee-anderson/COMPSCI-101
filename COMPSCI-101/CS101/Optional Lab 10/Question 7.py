term = 2


def get_sequence_number(term):
    # Handle the base cases directly
    if term == 0:
        return 0
    elif term == 1:
        return 0
    elif term == 2:
        return 1

    # Initialize the first three terams
    t0, t1, t2 = 0, 0, 1

    # Calculate the nth term iteratively
    for i in range(3, term + 1):
        next_term = t0 + t1 + t2
        t0, t1, t2 = t1, t2, next_term

    return t2


print("Term", term,"of the sequence is", get_sequence_number(term))