import json
from write_json import write_json
from genres_check import genres_check

filename = 'genres.json'

def genre_add():
    with open(filename) as json_file:
        data = json.load(json_file)

        temp = data['genres']

        # python object to be appended
        genre = input("\nPlease enter a genre: \n")
        y = {
                "genre": genre
            }

        #check if genre is already present, if yes quit application
        genres_check(genre)

        # appending data to books.json
        temp.append(y)
        write_json(data, filename)
        print("\nGenre added.")