import math
start = int(input("Enter the start: "))
end = int(input("Enter the end: "))

for i in range(start, end):
    if (math.sqrt(i)).is_integer():
        print(i, end=' ')
