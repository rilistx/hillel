import psycopg2
from connect_db import connection_database


# Insert Into to Table DATABASE
def insert_into_table_db(connection, insert_into_query, data):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(insert_into_query, data)
        print("Query executed successfully")
    except psycopg2.OperationalError as DB_ERROR:
        print(f"The error '{DB_ERROR}' occurred!")


users = [
    ('James', 25, 'male', 'USA'),
    ('Leila', 32, 'female', 'France'),
    ('Brigitte', 35, 'female', 'England'),
    ('Mike', 40, 'male', 'Denmark'),
    ('Elizabeth', 21, 'female', 'Canada'),
]

posts = [
    ("Happy", "I am feeling very happy today", 1),
    ("Hot Weather", "The weather is very hot today", 2),
    ("Help", "I need some help with my work", 2),
    ("Great News", "I am getting married", 1),
    ("Interesting Game", "It was a fantastic game of tennis", 5),
    ("Party", "Anyone up for a late-night party today?", 3),
]

comments = [
    ('Count me in', 1, 6),
    ('What sort of help?', 5, 3),
    ('Congrats buddy', 2, 4),
    ('I was rooting for Nadal though', 4, 5),
    ('Help with your thesis?', 2, 3),
    ('Many congratulations', 5, 4),
]

likes = [
    (1, 6),
    (2, 3),
    (1, 5),
    (5, 4),
    (2, 4),
    (4, 2),
    (3, 6),
]


user_records = ", ".join(["%s"] * len(users))
post_records = ", ".join(["%s"] * len(posts))
comment_records = ", ".join(["%s"] * len(comments))
like_records = ", ".join(["%s"] * len(likes))


insert_into_users_table = (
    f"INSERT INTO users (name, age, gender, nationality) VALUES {user_records}"
)

insert_into_posts_table = (
    f"INSERT INTO posts (title, description, user_id) VALUES {post_records}"
)

insert_into_comments_table = (
    f"INSERT INTO comments (text, user_id, post_id) VALUES {comment_records}"
)

insert_into_likes_table = (
    f"INSERT INTO likes (user_id, post_id) VALUES {like_records}"
)


if __name__ == "__main__":
    insert_into_table_db(connection_database, insert_into_users_table, users)
    insert_into_table_db(connection_database, insert_into_posts_table, posts)
    insert_into_table_db(connection_database, insert_into_comments_table, comments)
    insert_into_table_db(connection_database, insert_into_likes_table, likes)
