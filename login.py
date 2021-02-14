from select_permission import select_permission

def login():

    #get information if the person is admin or user
    permission = select_permission()

    #hardcoded username and password
    valid_username = 'admin'
    valid_password = '1234'

    #if the person is an admin, let them enter a username and password, which is checked. repeat until correct data is entered.
    if permission == '1':
        while (True):
            entered_username = input("\nPlease enter your username (username is admin): \n")
            entered_password = input("\nPlease enter your password (password is 1234): \n")
            if entered_username == valid_username and entered_password == valid_password:
                break
            else:
                print('\nUsername and/or Password incorrect.')

    #if the persin is an user, assigns the corresponding value without the need to login
    elif permission == '2':
        entered_username = 'user'
    
    return entered_username