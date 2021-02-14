import json

#function to check if a genre already exists
def genres_check(genreName):
    with open('genres.json') as json_file:
        data = json.load(json_file)

    #delcare variables for incoming loop
    available_genres = []
    counter = 0

    #check if a genre already exists
    for genre in data['genres']:
        if genreName in genre['genre']: 
            counter = counter + 1
    
    #if a genre was found, quit the program
    if counter >= 1:
        print("\nThis genry already exists.")
        quit()