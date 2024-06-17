def filter_positive_list(raw_data):
    i = 0
    while i < len(raw_data):
        if raw_data[i] < 1:
            raw_data.pop(i)
        else:
            i += 1
    return raw_data
