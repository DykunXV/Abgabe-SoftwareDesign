import json

def write_json(data, filename):

    #open a file and write data to it
    with open(filename,'w') as f:
        json.dump(data, f, indent=4)