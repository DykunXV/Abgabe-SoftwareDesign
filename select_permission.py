def select_permission():

    #let the person choose if they are an admin or user. repeat until a correct choice is entered
    while (True):
        selected_permission = input("\nPlease select your permission from the following options \n"
                          "1. Admin \n"
                          "2. User \n")
        if selected_permission == '1' or selected_permission == '2':
            break
        else:
            print('\nIncorrect choice. Please choose a correct option.')

    return selected_permission