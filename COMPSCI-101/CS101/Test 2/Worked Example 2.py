list1 = [1, 3, 5, 7, 9, 11, 13]
list2 = [0, 2, 4, 6, 8, 10, 12]
totals = []

for i in range(len(list1)):
    total = list1[i] + list2[(i + 1) % len(list2)]
    totals.append(total)
print(f"List of totals: {totals}")