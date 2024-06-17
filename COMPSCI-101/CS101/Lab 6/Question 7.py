grade = (input("Enter a grade (blank to exit): "))
total_grade = []

while grade != '':
    grade = int(grade)
    total_grade = total_grade + [grade]
    grade = (input("Enter a grade (blank to exit): "))

print(f"Grades: {total_grade}.")

if  total_grade != []:
    average = round(sum(total_grade) / len(total_grade), 1)

    print(f"The minimum grade is {min(total_grade)}.")
    print(f"The maximum grade is {max(total_grade)}.")
    print(f"The average grade is {average}.")




