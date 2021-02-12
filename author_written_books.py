import sys
import json


def author_written_books(selected_author_surname, selected_author_name):

    with open('books.json') as json_file:
        data = json.load(json_file)


    sorted_data = data
    sorted_data['books'] = sorted(data['books'], key=lambda x : x['title'], reverse=False)


    found_books = []
    counter = 0

    for book in sorted_data['books']:
        if selected_author_surname in book['authors'] and selected_author_name in book['authors']:
            counter = counter + 1
    

    return counter