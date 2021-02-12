from login import login

def selection_permission():
    permission = login()

    if permission == 'admin':
        valid_selections = ('1', '2', '3', '4', '5', '6')
        while (True):

            selection = input("\nPlease select from the following menu \n"
                            "1. Search Book by Name or ISBN\n"
                            "2. Search Book by Genre \n"
                            "3. Search Author \n"
                            "4. Add new Book\n"
                            "5. Add new Genre \n"
                            "6. Add new Author \n")
        
            if selection in valid_selections:
                break

            else:
                print('\nIncorrect choice. Please choose a correct option.')

        return selection

    elif permission == 'user':
        valid_selections = ('1', '2', '3')
        while (True):

            selection = input("\nPlease select from the following menu \n"
                            "1. Search Book by Name or ISBN \n"
                            "2. Search Book by Genre \n"
                            "3. Search Author \n")
        
            if selection in valid_selections:
                break

            else:
                print('\nIncorrect choice. Please choose a correct option.')

        return selection