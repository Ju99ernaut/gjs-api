import dataset

import config
from constants import *

from utils.db import connect_db

"""Functions for managing a dataset SQL database
    # Schemas

    #################### table ######################
    column1
    column2

"""


@connect_db
def add_item(db, column1, column2):
    table = db[TABLE]
    table.upsert(
        {
            COLUMN1_KEY: column1,
            COLUMN2_KEY: column2,
        },
        [COLUMN1_KEY, COLUMN2_KEY],
    )


@connect_db
def remove_item(db, column1, column2):
    table = db[TABLE]
    table.delete(column1=column1, column2=column2)


@connect_db
def get_item(db, column1):
    table = db[TABLE]
    row = table.find_one(column1=column1)
    if row is not None:
        return row[COLUMN2_KEY]
    return None


@connect_db
def get_all_items(db):
    table = db[TABLE]
    all_items = table.all()
    return all_items