import sys
import json

def book_search():
    with open('books.json') as json_file:
        data = json.load(json_file)

    #sort books by title in ascending order
    sorted_data = data
    sorted_data['books'] = sorted(data['books'], key=lambda x : x['title'], reverse=False)

    #delcare variables for incoming loop
    found_books = []
    isbn_found_books = []
    counter = 0

    #let the user enter a input to be searched. lists results. if no results are found, repeat.
    while (True):
        search_input = input("\nPlease enter the name or ISBN of the book you are looking for. \n")
        for book in sorted_data['books']:
            if search_input in book['title'] or search_input in book['isbn-13']:
                book_info = str(counter + 1) + ". " + book['title']
                found_books.append(book_info)
                isbn_found_books.append(book['isbn-13'])
                counter = counter + 1
        if counter != 0:
            print('\nFound', counter, 'result(s).')
            print(found_books)
            break
        else:
            print('\nNo books found.')

    #choose position of the book, in the array of books. if input is 0, quits the program.
    while (True):
        while (True):
            try:
                selection = int(input("\nPlease enter the position of book you want to know more about. Enter 0 to quit.\n")) - 1
                break
            except ValueError:
                print("\nYou entered something that wasn't a number.")
        try:
            selected_book_isbn = isbn_found_books[selection]
            break
        except IndexError:
            print("\nNo book exists at that position.")
    if selection == -1:
        quit()


    #find the book with the corresponding ISBN in books.json and print out available information
    for book in sorted_data['books']:
        if selected_book_isbn in book['isbn-13']:
            print('\nTitle:', book['title'])
            print('Published:', book['published'])
            print('Author:', book['authors'])
            print('Publisher:', book['publisher'])
            print('ISBN:', book['isbn-13'])
            print('Genre:', book['genre'])
            print('Pages:', book['pages'])