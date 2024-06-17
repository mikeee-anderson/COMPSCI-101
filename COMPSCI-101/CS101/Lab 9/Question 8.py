x = float(input("Enter x: "))
series = int(input("Enter the number of terms in the series: "))
f = 1 / (1 - x)
n = 0
for i in range(0, series + 1):
    n += x ** i

final = round(f - n, 6)
f = round(f, 6)
print(f"1 / (1 - {x}) = {f}")
print(f"The series with {series} terms differs by {final}")

