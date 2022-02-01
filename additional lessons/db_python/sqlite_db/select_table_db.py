import sqlite3

from connect_db import connection_database


# Select Query for DATEBASE
def query_select_db(connection, query):
    cursor = connection.cursor()
    result_query = None
    try:
        cursor.execute(query)
        result_query = cursor.fetchall()
        return result_query
    except sqlite3.OperationalError as DB_ERROR:
        print(f"The error '{DB_ERROR}' occurred!")


# Select from Table DATABASE
select_users_db = """
    SELECT
        *
    from
        users
"""

select_posts_db = """
    SELECT
        *
    from
        posts
"""

select_comments_db = """
    SELECT
        *
    from
        comments
"""

select_likes_db = """
    SELECT
        *
    from
        likes
"""


if __name__ == "__main__":
    users = query_select_db(connection_database, select_users_db)

    # Print USERS
    for user in users:
        print(user)

    print("\n#################################\n")

    posts = query_select_db(connection_database, select_posts_db)

    # Print POSTS
    for post in posts:
        print(post)

    print("\n#################################\n")

    comments = query_select_db(connection_database, select_comments_db)

    # Print COMMENTS
    for comment in comments:
        print(comment)

    print("\n#################################\n")

    likes = query_select_db(connection_database, select_likes_db)

    # Print LIKES
    for like in likes:
        print(like)
