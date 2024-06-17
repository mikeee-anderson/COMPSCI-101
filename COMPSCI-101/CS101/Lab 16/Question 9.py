letter_freq_dict1 = {"a": 1, "b": 2, "c": 3}
letter_freq_dict2 = {"d": 5, "b": 6, "e": 19}


def merge_frequency_dictionaries(dict1, dict2):
    # Create a new dictionary to store the merged results
    merged_dict = dict(dict1)  # Start with a copy of dict1

    # Iterate through dict2 and add the frequencies to merged_dict
    for key, value in dict2.items():
        if key in merged_dict:
            merged_dict[key] += value
        else:
            merged_dict[key] = value

    return merged_dict
merged_freq_dict = merge_frequency_dictionaries(letter_freq_dict1, letter_freq_dict2)
for key in sorted(merged_freq_dict):
    print(f"{key}: {merged_freq_dict[key]}")
print(type(merged_freq_dict))