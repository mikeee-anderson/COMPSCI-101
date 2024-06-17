grade_dict = {"Peter":"B", "Jane":"A", "Kathy":"A", "Mark":"A", "Tom":"C"}

def print_students_with_target_grade(grade_dict, target_grade):
   keys_list = list(grade_dict)
   counter = 0
   for key in keys_list:
      if grade_dict[key] != target_grade:
         del grade_dict[key]
      else:
         counter += 1
   if counter == 0:
      print(f"No students have the target grade {target_grade}")
   else:
      final_list = list(grade_dict)
      text = " "
      for names in final_list:
         text += names + " "
      print(f"The following students have the target grade {target_grade}:{text}")


def print_students_with_target_grade(grade_dict, target_grade):
   # Find all students with the target grade
   matching_students = [student for student, grade in grade_dict.items() if grade == target_grade]

   # Sort the list of matching students in ascending alphabetical order
   matching_students.sort()

   # Check if there are no students with the target grade
   if not matching_students:
      print(f"No students have the target grade {target_grade}")
   else:
      # Join the list of matching students into a single string with spaces
      students_text = ' '.join(matching_students)
      print(f"The following students have the target grade {target_grade}: {students_text}")


target_grade = "C"
print_students_with_target_grade(grade_dict, target_grade)
target_grade = "B"
print_students_with_target_grade(grade_dict, target_grade)