a_dict = { 'l':[5], 's':[8], 't':[10, 3, 8, 5] }

def get_average(a_dict):
    average_dict = {}
    for key in a_dict:
        total = 0
        count = 0
        for number in a_dict[key]:
            total += number
            count += 1
        average = round(total / count, 2)
        average_dict[key] = average
    return average_dict







result = get_average(a_dict)
for key in sorted(result.keys()):
    print(key, ':', result[key])