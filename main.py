from os import listdir
from os.path import isfile, join
from methods import add_to_db
import json

BASE_PATH = 'allureReport/'

def file_list(directory='allureReport') -> list:
    '''
    Returns a list of all files in the specified directory.
    '''

    files = [f for f in listdir(directory) if isfile(join(directory, f))]
    print(files)
    return files

def make_dict(file_name: str) -> dict:
    '''
    Converts a json file to a dictionary.
    '''
    with open(file_name) as json_file:
        data = json.load(json_file)
    print(data)
    return data

def main():
    '''
    Main function.
    '''
    files = file_list()
    for file in files:
        data_dict = make_dict(BASE_PATH+file)
        add_to_db(data_dict)

if __name__ == "__main__":
    main()