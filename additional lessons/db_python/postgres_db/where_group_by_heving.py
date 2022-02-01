from connect_db import connection_database
from select_table_db import query_select_db


select_posts_likes_db = """
    SELECT
        description as Post,
        COUNT(likes.id) as Likes
    FROM
        likes,
        posts
    WHERE
        posts.id = likes.post_id
    GROUP BY
        posts.description
    ORDER BY
        posts.description ASC
"""


if __name__ == "__main__":
    posts_likes = query_select_db(connection_database, select_posts_likes_db)

    for post_like in posts_likes:
        print(post_like)
