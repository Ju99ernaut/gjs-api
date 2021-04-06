# Super FastAPI

A REST API boilerplate project using `fastapi` and `dataset`, setup for easy deployment on `heroku`.

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

## Usage

Clone the repo

```sh
$ git clone https://github.com/Ju99ernaut/super-fastapi.git
$ cd superfast-api
```

Create virtual enviroment

```sh
$ python -m venv venv
```

Activate virtual enviroment

Linux/MacOS: `source venv/bin/activate`
Windows: `.\venv\Scripts\Activate.ps1` or `.\venv\Scripts\activate`

Install dependencies

```sh
$ pip install -r requirements.txt`
```

Run

```sh
$ python api/main.py
```

The API should now be available at `http://127.0.0.1:8000` and the API documentation will be available at `/docs` or `/redoc`.

Depending on the type of database backend, you may also need to install a database specific driver package. For MySQL, this is MySQLdb, for Postgres its psycopg2. SQLite support is integrated into Python.

On heroku you may come across the `sqlalchemy.exc.NoSuchModuleError: Can't load plugin: sqlalchemy.dialects:postgres`, you can avoid it by replacing `postgres://...` with `postgresql://...` in your connection url, or you can handle for it programmatically using something like:

```py
url = url.replace("postgres:", "postgresql:")
```


## License

MIT
