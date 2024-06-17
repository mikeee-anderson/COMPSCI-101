movie = input("Please enter the movie name or end to print the list: ")

movie_list = []
while movie != "end":
    if movie not in movie_list:
        movie_list.append(movie)
    movie = input("Please enter the movie name or end to print the list: ")

movie_list.sort()
print(" ")
print("Movies List:")
print("==============")
index = 0
counter = 1
while index < len(movie_list):
    print(f"{counter}) {movie_list[index]}")
    counter += 1
    index += 1



