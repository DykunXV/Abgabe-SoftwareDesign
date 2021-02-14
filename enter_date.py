import re

pattern = "[^0-9.]"

def enter_date(data_type):

    #loop, until an correct date format is entered
    while (True):

        #depending if an author or book is added, display different text
        if data_type == 'books.json':
            date = input("\nPlease enter when the book was published in the format dd.mm.yy: \n")
        else:
            date = input("\nPlease enter the birthday of the author in the format dd.mm.yy: \n")

        #checks if the date format is correct
        if (re.search(pattern, date)):
            print('\nFormat is incorrect.')
        elif len(date) != 10:
            print('\nFormat is incorrect.')
        elif date[2] and date[5] != '.':
            print('\nFormat is incorrect.')
        else:
            break

    return date