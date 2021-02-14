import json


def author_check():

    #open authors.json
    with open('authors.json') as json_file:
        data = json.load(json_file)

    #delcare variables for incoming loop
    counter = 0

    #check if a author exists, if yes then add +1 to the counter
    for author in data['authors']:
        counter = counter + 1
    
    #quits the programm if there are no authors
    if counter == 0:
        print("\nThere are no authors. Books can't be added without authors. Please add an author first.")
        quit()