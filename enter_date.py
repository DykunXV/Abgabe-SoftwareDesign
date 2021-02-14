def enter_date(type):

    #loop, until an correct date format is entered
    while (True):

        #depending if an author or book is added, display different text
        if type == 'books.json':
            date = input("\nPlease enter when the book was published in the format dd.mm.yy: \n")
        else:
            date = input("\nPlease enter the birthday of the author in the format dd.mm.yy: \n")

        #checks if the date format is correct
        if len(date) != 10:
            print('\nFormat is incorrect.')
        elif date[2] and date[5] != '.':
            print('\nFormat is incorrect.')
        elif int(date[0]) >= 3 and int(date[1]) >= 2:
            print('\nNo such date exists')
        elif int(date[3]) >= 1 and int(date[4]) >= 3:
            print('\nNo such date exists.')
        else:
            break

    return date