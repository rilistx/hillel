from connect_db import connection_database
from select_table_db import query_select_db


select_users_posts_db = """
    SELECT
        users.id,
        users.name,
        posts.description
    FROM
        posts
    INNER JOIN
        users
    ON
        users.id = posts.user_id
"""

select_users_posts_comments = """
    SELECT
        posts.description as post,
        text as comment,
        name
    FROM
        posts
    INNER JOIN
        comments
    ON
        posts.id = comments.post_id
    INNER JOIN
        users
    ON
        users.id = comments.user_id
"""


if __name__ == "__main__":
    users_posts = query_select_db(connection_database, select_users_posts_db)

    for user_post in users_posts:
        print(user_post)

    print("\n#################################\n")

    users_posts_comments = query_select_db(
        connection_database, select_users_posts_comments
    )

    for user_post_comment in users_posts_comments:
        print(user_post_comment)
