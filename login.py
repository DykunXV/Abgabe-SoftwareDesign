from select_permission import select_permission

def login():

    permission = select_permission()

    #hardcoded username and password
    valid_username = 'admin'
    valid_password = '1234'

    if permission == '1':

        while (True):
            entered_username = input("\nPlease enter your username (username is admin): \n")
            entered_password = input("\nPlease enter your password (password is 1234): \n")
        
            if entered_username == valid_username and entered_password == valid_password:
                break

            else:
                print('\nUsername and/or Password incorrect.')

    elif permission == '2':
        entered_username = 'user'
    
    return entered_username