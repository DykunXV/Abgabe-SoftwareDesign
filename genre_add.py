import json
from write_json import write_json
from genres_check import genres_check

filename = 'genres.json'

def genre_add():

    #open genres.json
    with open(filename) as json_file:
        data = json.load(json_file)
        temp = data['genres']

    #define the data that will be appended
    genre = input("\nPlease enter a genre: \n")
    y = {
            "genre": genre
        }

    #check if the entered genre already exists. if yes, quits application
    genres_check(genre)

    # appending data to books.json
    temp.append(y)
    write_json(data, filename)
    print("\nGenre added.")