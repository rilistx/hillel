from connect_db import connection_database
from select_table_db import query_select_db
from create_table_db import query_to_db


select_post_description = """
    SELECT
        description
    FROM
        posts
    WHERE
        id = 2
"""


"""
    description = "The weather has become pleasant now"
    description = "The weather is very hot today"
"""

# Updste_entry_in_table
update_post_description = """
    UPDATE
        posts
    SET
        description = "The weather has become pleasant now"
    WHERE
        id = 2
"""


if __name__ == "__main__":
    old_post_description = query_select_db(connection_database, select_post_description)

    for descriptions in old_post_description:
        for description in descriptions:
            print(f"The was: '{description}'!")

    print("\n#################################\n")

    query_to_db(connection_database, update_post_description)

    new_post_description = query_select_db(connection_database, select_post_description)

    for descriptions in new_post_description:
        for description in descriptions:
            print(f"The now: '{description}'!")
