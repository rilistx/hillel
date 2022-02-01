import psycopg2

from config import DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT


#   CRUD   --->   ( CREATE, READ, UPDATE, DELETE )


# Connect to PostgreSQL DATABASE
def connection_db(db_name, db_user, db_password, db_host, db_port):
    connection = None
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("\nConnection to PostgreSQL DB successful\n")
    except psycopg2.OperationalError as DB_ERROR:
        print(f"The error '{DB_ERROR}' occurred!")

    return connection


connection_database = connection_db(DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT)
