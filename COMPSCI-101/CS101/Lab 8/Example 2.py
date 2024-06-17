line_of_marks = input("Please enter your marks: ")
marks_list = line_of_marks.split(" ")
print(marks_list)
total = 0
count = len(marks_list)
for mark in marks_list:
    mark = float(mark)
    total += mark
average = total / count

print("Your average mark is", round(average, 2))
