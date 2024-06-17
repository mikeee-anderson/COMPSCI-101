
def remove_name(names_list, index):
    print("'{}' is removed.".format(names_list[index]))
    names_list.pop(index)


names = ['Abby', 'Bella', 'Charlotte', 'Daisy', 'Ella', 'Faith', 'Grace']
remove_name(names, 0)