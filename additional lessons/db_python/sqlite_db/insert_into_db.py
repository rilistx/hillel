from create_table_db import query_to_db
from connect_db import connection_database


# Insert Into to Table DATABASE
insert_into_users_table = """
    INSERT INTO
        users (
            name, age, gender, nationality
        )
    VALUES
        ('James', 25, 'male', 'USA'),
        ('Leila', 32, 'female', 'France'),
        ('Brigitte', 35, 'female', 'England'),
        ('Mike', 40, 'male', 'Denmark'),
        ('Elizabeth', 21, 'female', 'Canada');
"""

insert_into_posts_table = """
    INSERT INTO
        posts (
            title, description, user_id
        )
    VALUES
        ("Happy", "I am feeling very happy today", 1),
        ("Hot Weather", "The weather is very hot today", 2),
        ("Help", "I need some help with my work", 2),
        ("Great News", "I am getting married", 1),
        ("Interesting Game", "It was a fantastic game of tennis", 5),
        ("Party", "Anyone up for a late-night party today?", 3);
"""

insert_into_comments_table = """
    INSERT INTO
        comments (text, user_id, post_id)
    VALUES
        ('Count me in', 1, 6),
        ('What sort of help?', 5, 3),
        ('Congrats buddy', 2, 4),
        ('I was rooting for Nadal though', 4, 5),
        ('Help with your thesis?', 2, 3),
        ('Many congratulations', 5, 4);
"""

insert_into_likes_table = """
    INSERT INTO
        likes (user_id, post_id)
    VALUES
        (1, 6),
        (2, 3),
        (1, 5),
        (5, 4),
        (2, 4),
        (4, 2),
        (3, 6);
"""

if __name__ == "__main__":
    query_to_db(connection_database, insert_into_users_table)
    query_to_db(connection_database, insert_into_posts_table)
    query_to_db(connection_database, insert_into_comments_table)
    query_to_db(connection_database, insert_into_likes_table)
