a_list = [('See You Again', 'Wiz Khalifa'), ('Gangnam Style', 'PSY')]

def create_artist_dictionary(song_tuples_list):
    song_dict = {}
    for tuple1 in song_tuples_list:
        song_dict[tuple1[1]] = tuple1[0]
    return song_dict


a_dict = create_artist_dictionary(a_list)
for key in sorted(a_dict):
    print(key, a_dict[key])