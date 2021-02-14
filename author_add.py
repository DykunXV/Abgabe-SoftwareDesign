import json
from write_json import write_json
from enter_date import enter_date
from enter_author_name import enter_author_name

surname = "surname"
name = "name"
filename = 'authors.json'


def author_add():

    #open authors.json
    with open(filename) as json_file:
        data = json.load(json_file)
        temp = data['authors']

    #define the data that will be appended
    author_surname = enter_author_name(surname)
    author_name = enter_author_name(name)
    author_birthday = enter_date(filename)
    author_gender = input("\nPlease enter the gender of the author: \n")
    y = {
            "surname": author_surname,
            "name": author_name,
            "birthday": author_birthday,
            "gender": author_gender,
        }

    #appending data to authors.json
    temp.append(y)
    write_json(data, filename)
    print("\nAuthor added.")