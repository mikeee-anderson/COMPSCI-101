tl = (3, 7, 2, 7, 7, 9, 7)
values = []
while 7 in tl:
    index = tl.index(7)
    values.append(index)
    tl = tl[index + 1:]
print(values)
