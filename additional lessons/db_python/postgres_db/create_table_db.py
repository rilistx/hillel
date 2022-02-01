import psycopg2
from connect_db import connection_database


# Query for DATABASE
def query_to_db(connection, query):
    # connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except psycopg2.OperationalError as DB_ERROR:
        print(f"The error '{DB_ERROR}' occurred!")


# Create Table in DATABASE
create_users_table = """
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER,
        gender TEXT,
        nationality TEXT
    );
"""

create_posts_table = """
    CREATE TABLE IF NOT EXISTS posts (
        id SERIAL PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT NOT NULL,
        user_id INTEGER REFERENCES users (id)
    );
"""

create_comments_table = """
    CREATE TABLE IF NOT EXISTS comments (
        id SERIAL PRIMARY KEY,
        text TEXT NOT NULL,
        user_id INTEGER REFERENCES users (id),
        post_id INTEGER REFERENCES posts (id)
    );
"""

create_likes_table = """
    CREATE TABLE IF NOT EXISTS likes (
        id SERIAL PRIMARY KEY,
        user_id INTEGER REFERENCES users (id),
        post_id INTEGER REFERENCES posts (id)
    );
"""

if __name__ == "__main__":
    query_to_db(connection_database, create_users_table)
    query_to_db(connection_database, create_posts_table)
    query_to_db(connection_database, create_comments_table)
    query_to_db(connection_database, create_likes_table)
