import json

def choose_genre():

    #open genres.json
    with open('genres.json') as json_file:
        data = json.load(json_file)

    #declare variables for the incoming loop
    available_genres_numbered = []
    available_genres = []
    counter = 0

    #let the user enter a input to be searched. lists results. if no results are found, repeat.
    while (True):
        search_input = input("\nPlease enter the name of the genre you are looking for. \n")
        for genre in data['genres']:
            if search_input in genre['genre']:
                available_genres.append(genre['genre'])
                genre_numbered = str(counter + 1) + ". " + genre['genre']
                available_genres_numbered.append(genre_numbered)
                counter = counter + 1
        if counter != 0:
            print('\nFound', counter, 'result(s).')
            print(available_genres_numbered)
            break
        else:
            print('\nNo genres found.')

    #choose position of the genre, in the array of genres. if input is 0, quits the program.
    while (True):
        while (True):
            try:
                selection = int(input("\nPlease enter the position of the genre you are interested in. Enter 0 to quit.")) - 1
                break
            except ValueError:
                print("\nYou entered something that wasn't a number.")
        try:
            selected_genre = available_genres[selection]
            break
        except IndexError:
            print("\nNo genre exists at that position.")
    if selection == -1:
        quit()

    return selected_genre