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
    return files

def lines_from_file(file: str):
    lines = []
    with open(file, 'rt') as f:
        lines.append(f.readlines())
    return lines


def make_dict(file_name: str) -> dict:
    '''
    Converts a json file to a dictionary.
    '''
    with open(file_name) as json_file:
        data = json.load(json_file)
    return data


def upload_files_to_db():
    '''
    Main function: Scrapes allure report files and adds them to the database.
    Also, if the read file has the extension '.txt', it will be added to the text_config table.
    '''
    files = file_list()

    try:
        for file in files:
            if file.endswith('.json'):
                data_dict = make_dict(REPORT_PATH+file)
                add_to_db(data_dict)
            elif file.endswith('.txt'):
                lines_in_file = lines_from_file(REPORT_PATH+file)
                for line in lines_in_file:
                    write_to_config(line)
        
    except Exception as err:
        print(f'Could not upload to database. Err: {err}')


if __name__ == "__main__":
    # upload_files_to_db()
    print(retrieve_from_db())
