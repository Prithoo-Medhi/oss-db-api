from os import listdir, sep 
from os.path import isfile
from methods import add_to_db, retrieve_from_db, write_to_config
import json
from typing import List
## For Linux:
import pwd
from os import getuid

## For Linux:
REPORT_PATH = f'{sep}home{sep}{pwd.getpwuid(getuid())[0]}{sep}Coding{sep}oss-db-api{sep}allureReport{sep}'

## For Windows:
# REPORT_PATH = f"D:{sep}Libraries{sep}Arkiralor's Documents{sep}Programs{sep}gits{sep}oss-db-api{sep}allureReport{sep}"
# REPORT_PATH = f"allureReport{sep}"


def file_list(directory=REPORT_PATH) -> list:
    '''
    Returns a list of all files in the specified directory.
    '''
    files = [f for f in listdir(directory) if isfile(directory+f)]
    return files

def lines_from_file(file: str):
    '''
    Returns a list of all the lines in the file as iterables.
    '''
    lines = []
    with open(file, 'rt') as f:
        lines.extend(f.readlines())
    return lines


def make_dict(file_name: str) -> dict:
    '''
    Converts a json file to a dictionary.
    '''
    with open(file_name) as json_file:
        data = json.load(json_file)
    name = file_name.split(sep)
    name = name[len(name)-1]
    data['filename'] = name
    return data


def upload_files_to_db():
    '''
    Main function: Scrapes allure report files and adds them to the database.
    Also, if the read file has the extension '.txt', it will be added to the text_config table.
    '''
    files = file_list()
    
    for file in files:
        try:
            if file.endswith('.json'):
                data_dict = make_dict(REPORT_PATH+file)
                add_to_db(data_dict)
            elif file.endswith('.txt'):
                lines_in_file = lines_from_file(REPORT_PATH+file)
                for line in lines_in_file:
                    write_to_config(line)
        
        except Exception as err:
            print(f'Could not upload to database. Err: {err}')

def write_to_files(files: List[dict]):
    '''
    Write the output to a list of files.
    '''
    for item in files:
        with open(f'output/{item["filename"]}', 'wt') as file:
            del item['filename']
            json.dump(item, file)



if __name__ == "__main__":
    # upload_files_to_db()
    opt = retrieve_from_db()
    write_to_files(opt)
    print(opt)
