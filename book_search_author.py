import sys
import json

#the following function is the function that will be used to display the first three books of an author
def book_search_author(selected_author_surname, selected_author_name):

    #open books.json
    with open('books.json') as json_file:
        data = json.load(json_file)

    #sorts the results in ascending order, by title
    sorted_data = data
    sorted_data['books'] = sorted(data['books'], key=lambda x : x['title'], reverse=False)

    #delcare variables for incoming loop
    found_books = []
    counter = 0

    #create a for-loop until a maximum of 3 books of the author are found
    for book in sorted_data['books']:
        if selected_author_surname in book['authors'] and selected_author_name in book['authors']:
            book_info = book['title'] + " | " + book['published']
            found_books.append(book_info)
            counter = counter + 1
            if counter == 3:
                break
    

    #if books were found, return the array of founds books. oterhwise return the string that no books were found. 
    if counter >= 1:
        return found_books
    else:
        no_books = "This author hasn't written any books yet"
        return no_books