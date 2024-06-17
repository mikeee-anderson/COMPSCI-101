def save_names(filename, names_list):
    output_stream = open(filename, "w")
    for name in names_list:
        output_stream.write(name + "\n")
    output_stream.close()


names = names = ['Abby', 'Bella', 'Charlotte', 'Daisy', 'Ella', 'Faith', 'Grace']
save_names("names.txt", names)
