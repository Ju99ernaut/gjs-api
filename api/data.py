import dataset

import config
from constants import TEMPLATES_TABLE, ID_KEY

from utils.db import connect_db

"""Functions for managing a dataset SQL database
    # Schemas

    #################### templates ######################
    id
    name
    description
    assets
    template
    thumbnail
    pages
    styles
    updated_at

"""


@connect_db
def setup(db):
    db.create_table(TEMPLATES_TABLE, primary_id=ID_KEY, primary_type=db.types.string)


@connect_db
def add_template(db, template):
    table = db[TEMPLATES_TABLE]
    template[ID_KEY] = str(template[ID_KEY])
    table.upsert(template, [ID_KEY])


@connect_db
def remove_template(db, id):
    table = db[TEMPLATES_TABLE]
    table.delete(id=str(id))


@connect_db
def get_template(db, id):
    table = db[TEMPLATES_TABLE]
    row = table.find_one(id=str(id))
    if row is not None:
        return row
    return None


@connect_db
def get_all_templates(db):
    table = db[TEMPLATES_TABLE]
    return table.all()