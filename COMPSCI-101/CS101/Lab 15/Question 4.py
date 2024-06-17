band_list = [("Faith No More","Alternative"), ("Iron Maiden", "Metal"),
             ("Megadeth", "Metal"), ("Social Distortion", "Punk")]

def count_bands_per_genre(band_list):
    dictionary = {}
    for band in band_list:
        band = list(band)
        if band[1] in dictionary:
            dictionary[band[1]] += 1
        else:
            dictionary[band[1]] = 1
    return dictionary

genre_dict = count_bands_per_genre(band_list)
for key in sorted(genre_dict):
    print(key, genre_dict[key])