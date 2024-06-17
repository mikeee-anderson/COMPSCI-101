def read_lines(filename):
    input_stream = open(filename, "r")
    lines = input_stream.read().split("\n")
    input_stream.close()
    return lines

def create_country_tuples(lines):
    outcome = []
    for line in lines:
        parts = line.split(",")
        if len(parts) == 3:
            country = parts[0]
            language = parts[1]
            capital_city = parts[2]
            country_tuple = (country, language, capital_city)
            outcome.append(country_tuple)
    return outcome

lines = read_lines('country3.txt')
print(lines)
tuples = create_country_tuples(lines )
print(tuples)
