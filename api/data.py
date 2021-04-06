import dataset

import config
from constants import *

from utils.db import connect_db

"""Functions for managing a dataset SQL database
    # Schemas

    #################### table ######################
    id
    idx
    assets
    template
    thumbnail
    html
    css
    components
    styles

"""


@connect_db
def setup(db):
    db.create_table(TEMPLATES_TABLE, primary_id=IDX_KEY, primary_type=db.types.text)


@connect_db
def add_template(db, template):
    table = db[TEMPLATES_TABLE]
    table.upsert(template, [IDX_KEY])


@connect_db
def remove_template(db, idx):
    table = db[TEMPLATES_TABLE]
    table.delete(idx=idx)


@connect_db
def get_template(db, idx):
    table = db[TEMPLATES_TABLE]
    row = table.find_one(idx=idx)
    if row is not None:
        return row
    return None


@connect_db
def get_all_templates(db):
    table = db[TEMPLATES_TABLE]
    return table.all()