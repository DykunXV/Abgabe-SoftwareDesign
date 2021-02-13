import json

def choose_author():
    with open('authors.json') as json_file:
        data = json.load(json_file)

    #delcare variables for incoming loop
    found_authors = []
    surnames = []
    names = []
    counter = 0

    while (True):
        search_input = input("\nPlease enter the name or surname of the author you are looking for. \n")
        for author in data['authors']:
            if search_input in author['surname'] or search_input in author['name']:
                surnames.append(author['surname'])
                names.append(author['name'])
                full_name_numbered = str(counter + 1) + ". " + surnames[counter] + " " + names[counter]
                found_authors.append(full_name_numbered)
                counter = counter + 1
        
        if counter != 0:
            print('\nFound', counter, 'result(s).')
            print(found_authors)
            break
        else:
            print('\nNo authors found.')

    #Choose position of the author, in the array of authors
    while (True):
        while (True):
            try:
                selection = int(input("\nPlease enter the position of author you want to choose. Enter 0 to quit.")) - 1
                break
            except ValueError:
                print("\nYou entered something that wasn't a number.")
        try:
            selected_author_surname = surnames[selection]
            selected_author_name = names[selection]
            break
        except IndexError:
            print("\nNo author exists at that position.")
    
    if selection == -1:
        quit()

    #add name to surname and return the full name
    selected_author = selected_author_surname + " " + selected_author_name
    return selected_author