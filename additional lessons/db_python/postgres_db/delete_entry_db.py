from connect_db import connection_database
from select_table_db import query_select_db
from create_table_db import query_to_db


select_comments_table = """
    SELECT
        *
    FROM
        comments
"""

# Delete_entry_from_table
delete_comment = """
    DELETE FROM
        comments
    WHERE
        id = 5
"""


if __name__ == "__main__":
    old_comments_table = query_select_db(connection_database, select_comments_table)

    for comment in old_comments_table:
        print(comment)

    print("\n#################################\n")

    query_to_db(connection_database, delete_comment)

    new_comments_table = query_select_db(connection_database, select_comments_table)

    for comment in new_comments_table:
        print(comment)
