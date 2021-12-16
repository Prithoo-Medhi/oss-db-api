'''
Contains all functional methods (non-OOP) for the module.
'''

import psycopg2 as pg
from datetime import datetime
from init import BASE_PATH
from database import PGDATABASE, PGHOST, PGPORT, PGUSER, PGPASSWORD, DB_TYPE
import models
from sqlalchemy.orm import Session
from database import SessionLocal
from typing import List
import serializers


def add_to_db(db = SessionLocal()):
    """
    Adds a new entry to the table.
    """
    device_type = 'Mobile'
    device_name = 'Samsung Galaxy S10'
    browser_name = 'Firefox 32.0'
    screen_resolution = '1920x1080'
    bs_run_mode = 'Headless'
    is_device_real = True
    network_type = '4G'


    new_entry = models.Caps(device_type = device_type,
                            device_name = device_name,
                            browser_name = browser_name,
                            screen_resolution = screen_resolution,
                            bs_run_mode = bs_run_mode,
                            is_device_real = is_device_real,
                            network_type = network_type)

    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)
    print(new_entry)

def retrieve_from_db(db = SessionLocal()):
    """
    Retrieves all entries from the table.
    """
    result_list = []
    caps_list = db.query(models.Caps).all()
    for item in caps_list:
        result_list.append(serializers.capmodel_to_capschema(item))
    return result_list

if __name__ == "__main__":
    add_to_db()
    returned_list=retrieve_from_db()
    print(returned_list)