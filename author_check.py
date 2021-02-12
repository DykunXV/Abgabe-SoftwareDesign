import json


def author_check():
    with open('authors.json') as json_file:
        data = json.load(json_file)

    #delcare variables for incoming loop
    counter = 0

    #check if a author exists
    for author in data['authors']:
        counter = counter + 1
    
    #quits the programm if there are no authors
    if counter == 0:
        print("\nThere are no authors. Books can't be added without authors. Please add an author first.")
        quit()