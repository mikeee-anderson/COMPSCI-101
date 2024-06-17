lower = int(input("Enter the lower bound: "))
high = int(input("Enter the upper bound: "))
total = 0
for i in range(lower, high + 1):
    if i % 3 == 0:
        total += i
    if i % 5 == 0:
        total += i

print(f"Sum of multiples within [{lower}, {high}] is {total}.")