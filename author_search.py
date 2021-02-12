import sys
import json
from book_search_author import book_search_author
from author_written_books import author_written_books

def author_search():
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
                selection = int(input("\nPlease enter the position of author you want to know more about. Enter 0 to quit.\n")) - 1
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


    #find the author with the corresponding name + surname in authors.json and print out available information
    for author in data['authors']:
        if selected_author_surname in author['surname'] and selected_author_name in author['name']:
            print('\nSurname:', author['surname'])
            print('Name:', author['name'])
            print('Birthday:', author['birthday'])
            print('Gender:', author['gender'])
            print('Written Books:', author_written_books(selected_author_surname, selected_author_name))
            print('Up to three Books by this author:', book_search_author(selected_author_surname, selected_author_name))