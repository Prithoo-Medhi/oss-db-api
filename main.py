from os import listdir, getuid
from os.path import isfile, join
from methods import add_to_db, retrieve_from_db, write_to_config
import json
import pwd

REPORT_PATH = f'/home/{pwd.getpwuid(getuid())[0]}/Coding/oss-db-api/allureReport/'


def file_list(directory=REPORT_PATH) -> list:
    '''
    Returns a list of all files in the specified directory.
    '''

    files = [f for f in listdir(directory) if isfile(join(directory, f))]
    # print(files)
    return files


def make_dict(file_name: str) -> dict:
    '''
    Converts a json file to a dictionary.
    '''
    with open(file_name) as json_file:
        data = json.load(json_file)
    # print(data)
    return data


def upload_files_to_db():
    '''
    Main function: Scrapes allure report files and adds them to the database.
    Also, if the read file has the extension '.txt', it will be added to the text_config table.
    '''
    files = file_list()
    for file in files:
        if file.endswith('.json'):
            data_dict = make_dict(REPORT_PATH+file)
            add_to_db(data_dict)
        elif file.endswith('.txt'):
            # TODO: Add line parser and add each line to a row in 'txt_config' table.
            pass


if __name__ == "__main__":
    upload_files_to_db()
    print(retrieve_from_db())
