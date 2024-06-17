
def read_lines(filename):
    input_stream = open(filename, "r")
    contents = input_stream.read().split()
    input_stream.close()
    return contents

def create_marks_tuples(lines):
    result = []
    for line in lines:
        parts = line.split(",")
        username = parts[0]
        test_score = int(parts[1])
        exam_score = int(parts[2])
        total_score = test_score + exam_score
        tuple1 = (username, total_score)
        result.append(tuple1)
    return result


lines = read_lines('marks2.txt')
tuples = create_marks_tuples(lines)
print(tuples)




