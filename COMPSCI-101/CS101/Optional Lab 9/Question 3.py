string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

zipped_string = ""
if len(string1) == len(string2):
    for i in range(len(string1)):
        zipped_string += string1[i]
        zipped_string += string2[i]
    print(f"The zipped string is: {zipped_string}")
else:
    print("Error: Only strings of the same length can be zipped!")
