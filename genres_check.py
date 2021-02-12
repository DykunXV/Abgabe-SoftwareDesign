import json

#function to check if a genre already exists
def genres_check(genreName):
    with open('genres.json') as json_file:
        data = json.load(json_file)

    #delcare variables for incoming loop
    available_genres = []
    counter = 0

    #check if a author exists
    for genre in data['genres']:
        if genreName in genre['genre']: 
            counter = counter + 1
    
    #quits the programm if there are no authors
    if counter >= 1:
        print("\nThis genry already exists.")
        quit()