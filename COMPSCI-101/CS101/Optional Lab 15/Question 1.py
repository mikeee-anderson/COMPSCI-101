a_list = [(2000, 'Dragon'),(2001, 'Snake'),(2002, 'Horse'),(2003, 'Sheep'),(2004, 'Monkey'),(2005, 'Rooster'),(2006, 'Dog'),(2007, 'Pig'),(2008, 'Rat'),(2009, 'Ox'),(2010, 'Tiger'),(2011, 'Hare')]
def create_zodiac_dictionary(zodiac_tuples_list):
    zodiac_dict = {}
    for tuple1 in zodiac_tuples_list:
        zodiac_dict[tuple1[0]] = tuple1[1]
    return zodiac_dict


a_dict = create_zodiac_dictionary(a_list)
print(a_dict[2000])
print(a_dict[2001])
print(a_dict[2002])