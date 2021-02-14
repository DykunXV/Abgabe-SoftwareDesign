import json
from write_json import write_json
from choose_author import choose_author
from choose_genre import choose_genre
from enter_date import enter_date
from author_check import author_check

filename = 'books.json'


def book_add():

    #check if an author has been added
    author_check()

    #open books.json
    with open(filename) as json_file:
        data = json.load(json_file)
        temp = data['books']


    #define the data that will be appended
    book_title = input("\nPlease enter the title of the book: \n")
    book_published = enter_date(filename)
    book_author = choose_author()
    book_publisher = input("\nPlease enter the publisher of the book: \n")
    book_isbn13 = input("\nPlease enter the ISBN of the book: \n")
    book_genre = choose_genre()
    book_pages = int(input("\nPlease enter the amount of pages of the book: \n"))
    y = {
            "title": book_title,
            "published": book_published,
            "authors": book_author,
            "publisher": book_publisher,
            "isbn-13": book_isbn13,
            "genre": book_genre,
            "pages": book_pages
        }

    #appending data to books.json
    temp.append(y)
    write_json(data, filename)
    print("\nBook added.")