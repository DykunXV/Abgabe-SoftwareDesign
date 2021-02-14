import re

pattern = "^[a-zA-Z0-9]+$"

def enter_genre():

    #loop, until an correct name is entered
    while (True):

        genre = input("\nPlease enter a genre: \n")

        #checks if the regular expression matches the entered name
        if (re.search(pattern, genre)):
            break
        else:
            print('\nFormat is incorrect.')

    return genre