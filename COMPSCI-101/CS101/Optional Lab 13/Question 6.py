
def process_student_data(filename):
    input_stream = open(filename, "r")
    contents = input_stream.read().split()
    names_list = []
    average_list = []
    for i in range(0, len(contents), 3):
        if i + 2 < len(contents):
            # Read the name, number, and grades from consecutive lines
            name = contents[i].strip(':')
            number = int(contents[i + 1])  # This can be used if needed later
            grades = list(map(int, contents[i + 2].split(',')))

            # Calculate the average of grades
            average = sum(grades) / len(grades) if grades else 0

            # Append to the respective lists
            names_list.append(name)
            average_list.append(average)
    for i in range(len(names_list)):
        print(f"")

    return names_list, average_list



filename = "StudentData1.txt"
process_student_data(filename)