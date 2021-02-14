from selection_permission import selection_permission
from book_add import book_add
from author_add import author_add
from genre_add import genre_add
from book_search import book_search
from author_search import author_search
from genre_search import genre_search

def options():

    #get selection
    selection = selection_permission()

    if selection == '1':
        book_search()

    elif selection == '2':
        genre_search()

    elif selection == '3':
        author_search()

    elif selection == '4':
        book_add()

    elif selection == '5':
        genre_add()

    elif selection == '6':
        author_add()