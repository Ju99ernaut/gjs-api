import os
import functools

import dataset
import config

db = None


def connect_db(function):
    """
    Decorator that creates a database object and inserts as its
    the first argument in the calling function.
    """

    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        result = None
        engine_kwargs = {}

        pool_size = os.getenv("POOL_SIZE")
        max_overflow = os.getenv("MAX_OVERFLOW")

        if pool_size:
            engine_kwargs["pool_size"] = int(pool_size)

        if max_overflow:
            engine_kwargs["max_overflow"] = int(max_overflow)

        try:
            url = config.CONFIG.database_connection
        except:
            url = os.getenv("DATABASE_URL")

        global db
        if not db:
            db = dataset.connect(url, engine_kwargs=engine_kwargs)

        try:
            result = function(db, *args, **kwargs)
        except:
            db.rollback()

        return result

    return wrapper
