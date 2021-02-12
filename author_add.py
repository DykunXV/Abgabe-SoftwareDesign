import json
from write_json import write_json
from enter_date import enter_date

filename = 'authors.json'

def author_add():
    with open('authors.json') as json_file:
        data = json.load(json_file)

        temp = data['authors']

        # python object to be appended
        author_surname = input("\nPlease enter the surname of the author: \n")
        author_name = input("\nPlease enter the name of the author: \n")
        author_birthday = enter_date(filename)
        author_gender = input("\nPlease enter the gender of the author: \n")
        y = {
                "surname": author_surname,
                "name": author_name,
                "birthday": author_birthday,
                "gender": author_gender,
            }

        # appending data to authors.json
        temp.append(y)
        write_json(data, filename)
        print("\nAuthor added.")