full_name = "Wysten Auden"
space_index = full_name.find(" ")
first_name = full_name[:space_index]
last_name = full_name[space_index + 1:]
first_letter = first_name[0]
initialled_name = first_letter + ". " + last_name
print(initialled_name)
