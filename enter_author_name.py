import re

pattern = "^[a-zA-Z0-9,.'-]+$"

def enter_author_name(data_type):

    #loop, until an correct name is entered
    while (True):

        #depending if an surname or name is added, display different text
        if data_type == "surname":
            name = input("\nPlease enter the surname of the author: \n")
        else:
            name = input("\nPlease enter the name of the author: \n")

        #checks if the regular expression matches the entered name
        if (re.search(pattern, name)):
            break
        else:
            print('\nFormat is incorrect.')

    return name