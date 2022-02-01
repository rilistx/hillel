import sqlite3


#   CRUD   --->   ( CREATE, READ, UPDATE, DELETE )


# Connect to SQLite DATABASE
def connection_db(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("\nConnection to SQLite DB successful\n")
    except sqlite3.OperationalError as DB_ERROR:
        print(f"The error '{DB_ERROR}' occurred!")

    return connection


connection_database = connection_db("./db.sqlite")
