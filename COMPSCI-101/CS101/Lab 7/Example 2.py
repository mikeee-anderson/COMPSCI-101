numbers = [1206, 1216, 475, 1038, 1481, 135]
search_numbers = [1038, 1367, 1206, 740, 1281, 1216]
indicies = []
index = 0
while index < len(search_numbers):
    if search_numbers[index] in numbers:
        position = numbers.index(search_numbers[index])
        indicies.append(position)
    index += 1
indicies.sort()


print("indices of the numbers found", indicies)