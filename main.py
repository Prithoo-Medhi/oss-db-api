from os import listdir
from os.path import isfile, join
from methods import add_to_db, retrieve_from_db
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
    Main function: Scrapes allure report files and adds them to the database.
    Also, if the read file has the extension '.txt', it will be added to the text_config table.
    '''
    files = file_list()
    for file in files:
        if file.endswith('.json'):
            data_dict = make_dict(BASE_PATH+file)
            add_to_db(data_dict)
        elif file.endswith('.txt'):
            pass
            # TODO: Add text_config table insertion.
if __name__ == "__main__":
    # main()
    print(retrieve_from_db())