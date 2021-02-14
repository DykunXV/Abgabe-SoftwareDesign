from login import login

def selection_permission():
    
    #get permission
    permission = login()

    #if the person is an admin
    if permission == 'admin':

        #declare valid choices
        valid_selections = ('1', '2', '3', '4', '5', '6')

        #let the person choose from six options. repeat until a correct option is chosen.
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

    #if the person is a user
    elif permission == 'user':

        #declare valid choices
        valid_selections = ('1', '2', '3')

        #let the person choose from three options. repeat until a correct option is chosen.
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